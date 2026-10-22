"""Terminal helpers: ANSI styling, progress bar, file links, raw key input."""

from __future__ import annotations

import os
import re
import select
import shutil
import signal
import sys
import termios
import tty
from dataclasses import dataclass

COLOR = sys.stdout.isatty()

_ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]|\x1b\]8;;[^\x1b]*\x1b\\")


def _sgr(code: str) -> str:
    return f"\x1b[{code}m" if COLOR else ""


RESET = _sgr("0")
BOLD = _sgr("1")
UNDERLINE = _sgr("4")
NO_UNDERLINE = _sgr("24")
REVERSE = _sgr("7")
RED = _sgr("31")
GREEN = _sgr("32")
YELLOW = _sgr("33")
BLUE = _sgr("34")
MAGENTA = _sgr("35")
CYAN = _sgr("36")
FG_RESET = _sgr("39")

CLEAR = "\x1b[H\x1b[2J\x1b[3J"
ALT_SCREEN_ON = "\x1b[?1049h"
ALT_SCREEN_OFF = "\x1b[?1049l"
HIDE_CURSOR = "\x1b[?25l"
SHOW_CURSOR = "\x1b[?25h"
CLEAR_TO_EOL = "\x1b[K"


def strip_ansi(text: str) -> str:
    return _ANSI_RE.sub("", text)


def visible_width(text: str) -> int:
    width = 0
    for ch in strip_ansi(text):
        width += 2 if ord(ch) > 0xFFFF or ord(ch) in (0x1F40D,) else 1
    return width


def move_to(row: int, col: int) -> str:
    return f"\x1b[{row + 1};{col + 1}H"


def term_size() -> tuple[int, int]:
    size = shutil.get_terminal_size(fallback=(80, 24))
    return size.columns, size.lines


def clear_terminal(out=sys.stdout) -> None:
    out.write(CLEAR)


def progress_bar(done: int, total: int, term_width: int) -> str:
    prefix = "Progress: ["
    postfix_width = len("] xxx/xxx")
    wrapper_width = len(prefix) + postfix_width
    if term_width < wrapper_width + 4:
        return f"Progress: {done}/{total}"
    width = term_width - wrapper_width
    filled = (width * done) // total if total else width
    parts = [prefix, GREEN, "#" * filled]
    if filled < width:
        parts.append(">")
    rest = width - filled
    if rest > 1:
        parts += [RED, "-" * (rest - 1)]
    parts += [FG_RESET, f"] {done:>3}/{total}"]
    return "".join(parts)


def emit_file_links() -> bool:
    return os.environ.get("TERM_PROGRAM") != "vscode"


def file_link(path: str, canonical: str | None, color: str) -> str:
    """Underlined, coloured path; an OSC 8 hyperlink when the terminal supports it."""
    if canonical and emit_file_links() and COLOR:
        visible = f"\x1b]8;;file://{canonical}\x1b\\{path}\x1b]8;;\x1b\\"
    else:
        visible = path
    return f"{color}{UNDERLINE}{visible}{FG_RESET}{NO_UNDERLINE}"


@dataclass(frozen=True, slots=True)
class Key:
    text: str


@dataclass(frozen=True, slots=True)
class Resize:
    width: int
    height: int


Event = Key | Resize

_KEY_NAMES = {
    "\x1b[A": "up",
    "\x1b[B": "down",
    "\x1b[H": "home",
    "\x1b[F": "end",
    "\x1b[1~": "home",
    "\x1b[4~": "end",
    "\x1bOH": "home",
    "\x1bOF": "end",
    "\r": "enter",
    "\n": "enter",
    "\x7f": "backspace",
    "\x08": "backspace",
    "\x1b": "esc",
    "\x03": "ctrl-c",
}


class RawTerminal:
    """Puts stdin in cbreak mode (no line buffering, no echo) and reports
    key presses and terminal resizes. Use as a context manager."""

    def __init__(self) -> None:
        self.fd = sys.stdin.fileno()
        self._saved: list | None = None
        self._wake_r, self._wake_w = os.pipe()
        os.set_blocking(self._wake_w, False)
        self._old_wakeup = -1
        self._old_handler = None

    def __enter__(self) -> RawTerminal:
        self._saved = termios.tcgetattr(self.fd)
        tty.setcbreak(self.fd, termios.TCSANOW)
        self._old_handler = signal.signal(signal.SIGWINCH, lambda *_: None)
        self._old_wakeup = signal.set_wakeup_fd(self._wake_w, warn_on_full_buffer=False)
        return self

    def __exit__(self, *_) -> None:
        signal.set_wakeup_fd(self._old_wakeup)
        if self._old_handler is not None:
            signal.signal(signal.SIGWINCH, self._old_handler)
        if self._saved is not None:
            termios.tcsetattr(self.fd, termios.TCSANOW, self._saved)
        os.close(self._wake_r)
        os.close(self._wake_w)

    def drain(self) -> None:
        """Throw away any input typed while we were busy."""
        while select.select([self.fd], [], [], 0)[0]:
            os.read(self.fd, 1024)

    def read_event(self, timeout: float | None) -> Event | None:
        ready, _, _ = select.select([self.fd, self._wake_r], [], [], timeout)
        if self._wake_r in ready:
            os.read(self._wake_r, 1024)
            return Resize(*term_size())
        if self.fd not in ready:
            return None
        data = os.read(self.fd, 64).decode("utf-8", "replace")
        if not data:
            return Key("ctrl-c")
        return Key(_KEY_NAMES.get(data, data))

    def read_line(self) -> str:
        """Read a line of input with echo, for the reset confirmation."""
        assert self._saved is not None
        termios.tcsetattr(self.fd, termios.TCSANOW, self._saved)
        try:
            return sys.stdin.readline()
        finally:
            tty.setcbreak(self.fd, termios.TCSANOW)


def press_enter_prompt() -> None:
    sys.stdout.flush()
    sys.stdin.readline()
    sys.stdout.write("\n")
