#!/usr/bin/env python3
"""pylings — small Python exercises, in order, one concept at a time.

Rustlings for Python. No dependencies: stdlib only, Python 3.11+.

    python3 pylings.py                # watch mode -- start here
    python3 pylings.py run [NAME]     # run the current (or a named) exercise
    python3 pylings.py check-all      # check every exercise
    python3 pylings.py hint [NAME]    # hint for the current (or a named) exercise
    python3 pylings.py reset NAME     # throw away your changes to one exercise
"""

from __future__ import annotations

import argparse
import sys

from _pylings.app_state import AppState
from _pylings.exercise import solution_link_line
from _pylings.term import FG_RESET, GREEN, clear_terminal, press_enter_prompt
from _pylings.watch import watch


def welcome(app: AppState) -> None:
    out = sys.stdout
    clear_terminal(out)
    out.write(f"{app.welcome_message}\n\nPress ENTER to continue ")
    press_enter_prompt()
    clear_terminal(out)
    out.flush()


def cmd_watch(app: AppState) -> int:
    if not sys.stdout.isatty():
        sys.exit("Unsupported or missing terminal/TTY")
    if not app.state_file_read:
        if app.welcome_message:
            welcome(app)
        # First run: find out what is already solved.
        first_pending = app.check_all()
        if first_pending is None:
            app.render_final_message()
            return 0
        app.set_current(first_pending)
    watch(app)
    return 0


def cmd_run(app: AppState, name: str | None) -> int:
    if name:
        app.set_current_by_name(name)
    out = sys.stdout
    exercise = app.current
    success, output = exercise.run()
    out.write(output)
    if not success:
        app.set_pending(app.current_ind)
        out.write(f"Ran {exercise.link()} with errors\n")
        return 1
    out.write(f"{GREEN}✓ Successfully ran {exercise.path}{FG_RESET}\n")
    if exercise.solution_path:
        out.write("\n" + solution_link_line(exercise.solution_path) + "\n")
    if not app.done_current(out, clear_before_final_check=False):
        out.write(f"Next exercise: {app.current.link()}\n")
    return 0


def cmd_check_all(app: AppState) -> int:
    out = sys.stdout
    first_pending = app.check_all(out)
    if first_pending is None:
        app.render_final_message(out)
        return 0
    if app.current.done:
        app.set_current(first_pending)
    out.write("\n\n")
    if app.n_pending == 1:
        out.write("One exercise pending: ")
    else:
        out.write(f"{app.n_pending}/{len(app.exercises)} exercises pending. The first: ")
    out.write(f"{app.current.link()}\n")
    return 1


def cmd_hint(app: AppState, name: str | None) -> int:
    if name:
        app.set_current_by_name(name)
    print(app.current.hint)
    return 0


def cmd_reset(app: AppState, name: str) -> int:
    app.set_current_by_name(name)
    path = app.reset(app.current_ind)
    print(f"The exercise {path} has been reset")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="pylings",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command")
    p_run = sub.add_parser("run", help="run a single exercise (the current one by default)")
    p_run.add_argument("name", nargs="?")
    sub.add_parser("check-all", help="check all exercises, marking them done or pending")
    p_hint = sub.add_parser("hint", help="show a hint (for the current exercise by default)")
    p_hint.add_argument("name", nargs="?")
    p_reset = sub.add_parser("reset", help="reset a single exercise")
    p_reset.add_argument("name")

    args = parser.parse_args(argv)
    app = AppState()
    try:
        match args.command:
            case "run":
                return cmd_run(app, args.name)
            case "check-all":
                return cmd_check_all(app)
            case "hint":
                return cmd_hint(app, args.name)
            case "reset":
                return cmd_reset(app, args.name)
            case _:
                return cmd_watch(app)
    except KeyboardInterrupt:
        print()
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
