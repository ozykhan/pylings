"""One exercise: where it lives, how to run it, how its output is shown."""

from __future__ import annotations

import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from .term import BLUE, BOLD, CYAN, RED, RESET, UNDERLINE, file_link

ROOT = Path(__file__).resolve().parent.parent
TIMEOUT = 30


def clean_traceback(text: str) -> str:
    """Drop frames inside pylings_check so the traceback points at your code,
    and show paths relative to the pylings directory."""
    text = text.replace(str(ROOT) + os.sep, "")
    out: list[str] = []
    skip = 0
    for line in text.splitlines():
        if skip:
            skip -= 1
            continue
        if line.lstrip().startswith('File "') and "pylings_check.py" in line:
            skip = 1  # also drop the source line that follows
            continue
        out.append(line)
    return "\n".join(out)


@dataclass(slots=True)
class Exercise:
    name: str
    path: str  # relative, posix, e.g. exercises/01_basics/basics1.py
    hint: str
    done: bool = False

    @property
    def abs_path(self) -> Path:
        return ROOT / self.path

    @property
    def solution_path(self) -> str | None:
        rel = self.path.replace("exercises/", "solutions/", 1)
        return rel if (ROOT / rel).exists() else None

    def link(self) -> str:
        return file_link(self.path, str(self.abs_path), BLUE)

    def run(self) -> tuple[bool, str]:
        """Run the exercise. Returns (success, output block)."""
        env = dict(os.environ)
        env["PYTHONPATH"] = str(ROOT) + os.pathsep + env.get("PYTHONPATH", "")
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        try:
            result = subprocess.run(
                [sys.executable, self.path],  # relative: keeps tracebacks short
                capture_output=True,
                text=True,
                cwd=str(ROOT),
                env=env,
                timeout=TIMEOUT,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            body = (exc.stdout or b"").decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            return False, _format(body, f"Timed out after {TIMEOUT}s. Infinite loop?", False)
        return result.returncode == 0, _format(result.stdout, clean_traceback(result.stderr), result.returncode == 0)


def _format(stdout: str, stderr: str, success: bool) -> str:
    parts = [f"{UNDERLINE}Output{RESET}\n"]
    if stdout.strip():
        parts.append(stdout.rstrip("\n") + "\n")
    if stderr.strip():
        parts.append(stderr.rstrip("\n") + "\n")
    if not success:
        parts.append(f"{BOLD}{RED}The exercise didn't run successfully (nonzero exit code){RESET}\n")
    return "".join(parts)


def solution_link_line(solution_path: str) -> str:
    return f"{BOLD}Solution{RESET} for comparison: {file_link(solution_path, str(ROOT / solution_path), CYAN)}\n"
