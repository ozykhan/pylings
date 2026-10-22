"""Watch mode: re-run the current exercise on save, drive it from the keyboard."""

from __future__ import annotations

import sys

from .app_state import AppState
from .exercise import solution_link_line
from .listmode import list_mode
from .term import (
    BOLD,
    CLEAR,
    CYAN,
    FG_RESET,
    GREEN,
    RESET,
    UNDERLINE,
    Key,
    RawTerminal,
    Resize,
    progress_bar,
    term_size,
)

POLL_SECONDS = 0.4

QUIT_MSG = """

We hope you're enjoying learning Python!
If you want to continue working on the exercises at a later point, you can simply run `python3 pylings.py` again in this directory.
"""


class WatchState:
    def __init__(self, app: AppState, term: RawTerminal) -> None:
        self.app = app
        self.term = term
        self.output = ""
        self.show_hint = False
        self.done = False
        self.solution: str | None = None
        self.term_width = term_size()[0]
        self.out = sys.stdout

    # -- running -----------------------------------------------------------

    def run_current(self) -> None:
        self.show_hint = False
        self.out.write(f"\nChecking the exercise `{self.app.current.name}`. Please wait…\n")
        self.out.flush()
        success, output = self.app.current.run()
        self.output = output + "\n"
        if success:
            self.done = True
            self.solution = self.app.current.solution_path
        else:
            self.done = False
            self.solution = None
            self.app.set_pending(self.app.current_ind)
        self.term.drain()
        self.render()

    def next_exercise(self) -> str:
        """Returns 'current_pending', 'new_pending' or 'all_done'."""
        if not self.done:
            return "current_pending"
        if self.app.done_current(self.out, clear_before_final_check=True):
            return "all_done"
        return "new_pending"

    def check_all(self) -> str:
        first_pending = self.app.check_all(self.out)
        self.term.drain()
        if first_pending is None:
            self.app.render_final_message(self.out)
            return "all_done"
        if self.app.current.done:
            self.app.set_current(first_pending)
            return "new_pending"
        return "current_pending"

    def reset_exercise(self) -> None:
        self.out.write(CLEAR)
        self.out.write(
            f"Resetting will undo all your changes to the file {self.app.current.path}\n"
            "Reset (y/n)? "
        )
        self.out.flush()
        while True:
            event = self.term.read_event(None)
            if not isinstance(event, Key):
                continue
            if event.text in ("y", "Y"):
                self.app.reset(self.app.current_ind)
                # The file watcher notices the change and re-runs the exercise.
                return
            if event.text in ("n", "N"):
                self.render()
                return

    def hint(self) -> None:
        if not self.show_hint:
            self.show_hint = True
            self.render()

    def update_term_width(self, width: int) -> None:
        if width != self.term_width:
            self.term_width = width
            self.render()

    # -- rendering ---------------------------------------------------------

    def prompt(self) -> str:
        parts: list[str] = []
        if self.done:
            parts.append(f"{BOLD}n{RESET}:{UNDERLINE}next{RESET} / ")
        if not self.show_hint:
            parts.append(f"{BOLD}h{RESET}:hint / ")
        parts.append(f"{BOLD}l{RESET}:list / ")
        parts.append(f"{BOLD}c{RESET}:check all / ")
        parts.append(f"{BOLD}x{RESET}:reset / ")
        parts.append(f"{BOLD}q{RESET}:quit ? ")
        return "".join(parts)

    def render(self) -> None:
        out = self.out
        # Prevent having the first line shifted if clearing wasn't successful.
        out.write("\n" + CLEAR)
        out.write(self.output)
        if self.show_hint:
            out.write(f"{BOLD}{UNDERLINE}{CYAN}Hint{RESET}\n{self.app.current.hint}\n\n")
        if self.done:
            out.write(f"{BOLD}{GREEN}Exercise done ✓{RESET}\n")
            if self.solution:
                out.write(solution_link_line(self.solution))
            out.write("When done experimenting, enter `n` to move on to the next exercise 🐍\n\n")
        out.write(progress_bar(self.app.n_done, len(self.app.exercises), self.term_width))
        out.write(f"\nCurrent exercise: {self.app.current.link()}\n\n")
        out.write(self.prompt())
        out.flush()


def _mtime(app: AppState) -> float:
    try:
        return app.current.abs_path.stat().st_mtime
    except FileNotFoundError:
        return 0.0


def _run_watch(app: AppState, term: RawTerminal) -> str:
    """Returns 'quit', 'done' or 'list'."""
    state = WatchState(app, term)
    state.run_current()
    mtime = _mtime(app)

    while True:
        event = term.read_event(POLL_SECONDS)
        if event is None:
            new_mtime = _mtime(app)
            if new_mtime != mtime:
                mtime = new_mtime
                state.run_current()
            continue
        if isinstance(event, Resize):
            state.update_term_width(event.width)
            continue

        match event.text:
            case "n":
                progress = state.next_exercise()
                if progress == "all_done":
                    return "done"
                if progress == "new_pending":
                    state.run_current()
                    mtime = _mtime(app)
            case "h":
                state.hint()
            case "l":
                return "list"
            case "c":
                progress = state.check_all()
                if progress == "all_done":
                    return "done"
                if progress == "new_pending":
                    state.run_current()
                    mtime = _mtime(app)
                else:
                    state.render()
            case "x":
                state.reset_exercise()
            case "q" | "ctrl-c":
                return "quit"
            case _:
                pass


def watch(app: AppState) -> None:
    with RawTerminal() as term:
        while True:
            match _run_watch(app, term):
                case "quit":
                    sys.stdout.write(QUIT_MSG)
                    return
                case "done":
                    return
                case "list":
                    # Leave watch mode, run the list, then restart watch mode.
                    list_mode(app, term)
