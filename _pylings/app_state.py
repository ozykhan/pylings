"""Which exercise is current, which are done, and the state file behind it."""

from __future__ import annotations

import queue
import shutil
import sys
import tomllib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .exercise import ROOT, Exercise
from .term import (
    BLUE,
    FG_RESET,
    GREEN,
    HIDE_CURSOR,
    RED,
    SHOW_CURSOR,
    clear_terminal,
    move_to,
    term_size,
)

STATE_FILE = ROOT / ".pylings-state.txt"
STATE_HEADER = "DON'T EDIT THIS FILE!\n\n"
INFO = ROOT / "info.toml"
PRISTINE = ROOT / ".pylings" / "pristine"

FINISH_LINE = """\
+----------------------------------------------------+
|          You made it to the finish line!           |
+--------------------------  ------------------------+
                           \\/
""" + GREEN + r"""
                  ____
                 /    \_____
                |  o o      \______
                 \    ____         \_____
                  \__/    \____         \____
                               \___          \___
              ___________________ \__           \
             /                     \ \___________/
            /    ______________     \
           |    /              \     |
           |   |                \    |
            \__/                 \___/
""" + FG_RESET


def parse_state(text: str) -> tuple[str, set[str]] | None:
    lines = text.split("\n")[2:]
    if not lines:
        return None
    current = lines[0]
    if not current or len(lines) < 2:
        return None
    done: set[str] = set()
    for name in lines[2:]:
        if not name:
            break
        done.add(name)
    return current, done


def render_state(current: str, done: list[str]) -> str:
    return STATE_HEADER + current + "\n" + "".join(f"\n{name}" for name in done)


def next_pending_index(done: list[bool], current: int) -> int | None:
    for ind in range(current + 1, len(done)):
        if not done[ind]:
            return ind
    for ind in range(current):
        if not done[ind]:
            return ind
    return None


class AppState:
    def __init__(self) -> None:
        if not INFO.exists():
            sys.exit("info.toml is missing. Are you in the pylings directory?")
        data = tomllib.loads(INFO.read_text(encoding="utf-8"))
        self.welcome_message: str = data.get("welcome_message", "").strip()
        self.final_message: str = data.get("final_message", "").strip()
        self.exercises: list[Exercise] = [
            Exercise(name=item["name"], path=item["path"], hint=item["hint"].strip())
            for item in data["exercises"]
        ]
        self.current_ind = 0
        self.state_file_read = False
        try:
            parsed = parse_state(STATE_FILE.read_text(encoding="utf-8"))
        except FileNotFoundError:
            parsed = None
        if parsed is not None:
            current, done = parsed
            for ind, ex in enumerate(self.exercises):
                ex.done = ex.name in done
                if ex.name == current:
                    self.current_ind = ind
            self.state_file_read = True

    # -- queries -----------------------------------------------------------

    @property
    def current(self) -> Exercise:
        return self.exercises[self.current_ind]

    @property
    def n_done(self) -> int:
        return sum(ex.done for ex in self.exercises)

    @property
    def n_pending(self) -> int:
        return len(self.exercises) - self.n_done

    def index_of(self, name: str) -> int:
        for ind, ex in enumerate(self.exercises):
            if ex.name == name:
                return ind
        matches = [ind for ind, ex in enumerate(self.exercises) if ex.name.startswith(name)]
        if len(matches) == 1:
            return matches[0]
        if matches:
            names = ", ".join(self.exercises[i].name for i in matches)
            sys.exit(f"'{name}' is ambiguous: {names}")
        sys.exit(f"No exercise found for '{name}'!")

    # -- mutations ---------------------------------------------------------

    def write(self) -> None:
        done = [ex.name for ex in self.exercises if ex.done]
        STATE_FILE.write_text(render_state(self.current.name, done), encoding="utf-8")

    def set_current(self, ind: int) -> None:
        if ind != self.current_ind:
            self.current_ind = ind
            self.write()

    def set_current_by_name(self, name: str) -> None:
        self.set_current(self.index_of(name))

    def set_status(self, ind: int, done: bool) -> bool:
        ex = self.exercises[ind]
        if ex.done == done:
            return False
        ex.done = done
        return True

    def set_pending(self, ind: int) -> None:
        if self.set_status(ind, False):
            self.write()

    def reset(self, ind: int) -> str:
        """Restore one exercise from its pristine copy. Returns its path."""
        self.set_pending(ind)
        ex = self.exercises[ind]
        backup = PRISTINE / Path(ex.path).relative_to("exercises")
        if not backup.exists():
            sys.exit(f"No pristine copy for {ex.name}. Run `python3 _build/build.py`.")
        shutil.copyfile(backup, ex.abs_path)
        return ex.path

    def done_current(self, out=sys.stdout, *, clear_before_final_check: bool) -> bool:
        """Mark the current exercise done and move to the next pending one.
        Returns True when every exercise is done."""
        self.current.done = True
        nxt = next_pending_index([ex.done for ex in self.exercises], self.current_ind)
        if nxt is not None:
            self.set_current(nxt)
            return False
        if clear_before_final_check:
            clear_terminal(out)
        else:
            out.write("\n")
        first_pending = self.check_all(out)
        if first_pending is not None:
            self.set_current(first_pending)
            return False
        self.render_final_message(out)
        return True

    # -- check all ---------------------------------------------------------

    def check_all(self, out=sys.stdout) -> int | None:
        """Run every exercise in parallel, drawing the coloured grid rustlings
        draws. Updates the state file. Returns the first pending index."""
        out.write(HIDE_CURSOR)
        try:
            return self._check_all(out)
        finally:
            out.write(SHOW_CURSOR)
            out.flush()

    def _check_all(self, out) -> int | None:
        width, _ = term_size()
        clear_terminal(out)
        out.write("Checking all exercises…\n")
        out.write(
            f"Color of exercise number: {BLUE}Checking{FG_RESET} - "
            f"{GREEN}Done{FG_RESET} - {RED}Pending{FG_RESET}\n"
        )
        n_cols = max(1, (width + 1) // 4)
        progress: list[str | None] = [None] * len(self.exercises)

        def draw() -> None:
            out.write(move_to(2, 0))
            for ind, state in enumerate(progress):
                color = {"checking": BLUE, "done": GREEN, "pending": RED}.get(state or "", "")
                out.write(f"{color}{ind + 1:<3}{FG_RESET}")
                if ind + 1 != len(progress):
                    out.write("\n" if (ind + 1) % n_cols == 0 else " ")
            out.flush()

        events: queue.Queue[tuple[int, str]] = queue.Queue()

        def work(ind: int) -> None:
            events.put((ind, "checking"))
            success, _ = self.exercises[ind].run()
            events.put((ind, "done" if success else "pending"))

        draw()
        with ThreadPoolExecutor() as pool:
            futures = [pool.submit(work, ind) for ind in range(len(self.exercises))]
            remaining = len(futures)
            while remaining:
                ind, state = events.get()
                progress[ind] = state
                if state != "checking":
                    remaining -= 1
                draw()
            for f in futures:
                f.result()

        first_pending: int | None = None
        for ind, state in enumerate(progress):
            done = state == "done"
            self.set_status(ind, done)
            if not done and first_pending is None:
                first_pending = ind
        self.write()
        return first_pending

    def render_final_message(self, out=sys.stdout) -> None:
        clear_terminal(out)
        out.write(FINISH_LINE)
        if self.final_message:
            out.write(self.final_message + "\n")
        out.flush()
