"""Generates exercises/, solutions/, info.toml and .pylings/pristine/."""

from __future__ import annotations

import importlib.util
import shutil
import textwrap
from pathlib import Path

BUILD = Path(__file__).resolve().parent
ROOT = BUILD.parent
HELPERS = ["eq", "is_", "ok", "not_ok", "raises"]

HEADER = """\
# {name}.py
#
{intro}
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.
"""

WELCOME_MESSAGE = """
       Welcome to...
                 _ _
      _ __  _   _| (_)_ __   __ _ ___
     | '_ \\| | | | | | '_ \\ / _` / __|
     | |_) | |_| | | | | | | (_| \\__ \\
     | .__/ \\__, |_|_|_| |_|\\__, |___/
     |_|    |___/            |___/

Is this your first time? Don't worry, pylings is made for beginners!
We are going to teach you a lot of things about Python, but before we can
get started, here are some notes about how pylings operates:

1. The central concept behind pylings is that you solve exercises. These
   exercises usually contain some code that fails to run or fails its checks.
   You need to edit the file to make it pass.
2. When you first run pylings, it checks every exercise and opens the first
   pending one in watch mode. Every time you save the file it re-runs the
   exercise. Once it passes, press `n` to move on to the next one.
3. If you're stuck on an exercise, press `h` for a hint. Press `l` to see
   every exercise, jump to one, or reset one.
4. If an exercise doesn't make sense to you, feel free to compare your
   solution with the one in `solutions/` after it passes.

Got all that? Great! Press ENTER and pylings will find your first exercise.
"""

FINAL_MESSAGE = """
Go build something. Then come back for the next section.
"""

SOLUTION_HEADER = """\
# {name}.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.
"""


def load_sections() -> list[tuple[str, list[dict[str, str]]]]:
    out = []
    for path in sorted((BUILD / "sections").glob("s*.py")):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        assert spec and spec.loader
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.append((mod.SECTION, mod.EXERCISES))
    return out


def comment(text: str) -> str:
    lines = []
    for raw in textwrap.dedent(text).strip().splitlines():
        lines.append(f"# {raw}".rstrip())
    return "\n".join(lines)


def imports_for(checks: str) -> str:
    used = [h for h in HELPERS if f"{h}(" in checks]
    return f"from pylings_check import {', '.join(used)}\n" if used else ""


def render(ex: dict[str, str], *, solved: bool) -> str:
    body = textwrap.dedent(ex["solution"] if solved else ex["stub"]).strip()
    checks = textwrap.dedent(ex["checks"]).strip()
    header = (
        SOLUTION_HEADER.format(name=ex["name"])
        if solved
        else HEADER.format(name=ex["name"], intro=comment(ex["intro"]))
    )
    return (
        f"{header}\n"
        f"{imports_for(checks)}\n"
        f"{body}\n\n\n"
        f"# --- checks (do not edit) ------------------------------------------\n"
        f"{checks}\n"
    )


def main() -> None:
    sections = load_sections()
    for target in ("exercises", "solutions", ".pylings/pristine"):
        shutil.rmtree(ROOT / target, ignore_errors=True)

    info: list[str] = [
        "# Hints for every exercise. pylings reads this.",
        "# Order matters: it is the order you work through them.",
        "",
        # Literal strings: the ASCII art has backslashes.
        "welcome_message = '''",
        WELCOME_MESSAGE.strip("\n"),
        "'''",
        "",
        "final_message = '''",
        FINAL_MESSAGE.strip("\n"),
        "'''",
        "",
    ]
    count = 0
    for section, exercises in sections:
        for ex in exercises:
            count += 1
            rel = Path(section) / f"{ex['name']}.py"
            for base, solved in ((ROOT / "exercises", False), (ROOT / "solutions", True)):
                path = base / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(render(ex, solved=solved), encoding="utf-8")
            pristine = ROOT / ".pylings" / "pristine" / rel
            pristine.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / "exercises" / rel, pristine)

            hint = textwrap.dedent(ex["hint"]).strip()
            info += [
                "[[exercises]]",
                f'name = "{ex["name"]}"',
                f'path = "exercises/{rel.as_posix()}"',
                'hint = """',
                hint,
                '"""',
                "",
            ]

    (ROOT / "info.toml").write_text("\n".join(info), encoding="utf-8")
    print(f"built {count} exercises across {len(sections)} sections")


if __name__ == "__main__":
    main()
