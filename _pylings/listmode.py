"""The list view: every exercise, its state, and where you are."""

from __future__ import annotations


class ScrollState:
    def __init__(self, n_rows: int, selected: int | None, max_scroll_padding: int) -> None:
        self.n_rows = n_rows
        self.max_n_rows_to_display = 0
        self.selected = selected
        self.offset = 0 if selected is None else max(0, selected - max_scroll_padding)
        self.scroll_padding = 0
        self.max_scroll_padding = max_scroll_padding

    def _update_offset(self) -> None:
        if self.selected is None:
            return
        min_offset = max(0, self.selected + self.scroll_padding - max(0, self.max_n_rows_to_display - 1))
        max_offset = max(0, self.selected - self.scroll_padding)
        global_max = max(0, self.n_rows - self.max_n_rows_to_display)
        self.offset = min(max(self.offset, min_offset), max_offset, global_max)

    def set_selected(self, selected: int) -> None:
        self.selected = selected
        self._update_offset()

    def select_next(self) -> None:
        if self.selected is not None:
            self.set_selected(min(self.selected + 1, self.n_rows - 1))

    def select_previous(self) -> None:
        if self.selected is not None:
            self.set_selected(max(self.selected - 1, 0))

    def select_first(self) -> None:
        if self.n_rows > 0:
            self.set_selected(0)

    def select_last(self) -> None:
        if self.n_rows > 0:
            self.set_selected(self.n_rows - 1)

    def set_n_rows(self, n_rows: int) -> None:
        self.n_rows = n_rows
        if n_rows == 0:
            self.selected = None
            return
        self.set_selected(0 if self.selected is None else min(self.selected, n_rows - 1))

    def set_max_n_rows_to_display(self, n: int) -> None:
        self.max_n_rows_to_display = n
        self.scroll_padding = min(n // 4, self.max_scroll_padding)
        self._update_offset()


import sys

from .app_state import AppState
from .exercise import Exercise
from .term import (
    ALT_SCREEN_OFF,
    ALT_SCREEN_ON,
    BOLD,
    CLEAR_TO_EOL,
    FG_RESET,
    GREEN,
    HIDE_CURSOR,
    MAGENTA,
    RED,
    RESET,
    REVERSE,
    SHOW_CURSOR,
    UNDERLINE,
    YELLOW,
    Key,
    RawTerminal,
    Resize,
    move_to,
    progress_bar,
    term_size,
)

COL_SPACING = 2
SNAKE = "🐍"


class Row:
    """Accumulates one screen row, refusing text past the terminal width."""

    def __init__(self, max_len: int) -> None:
        self.parts: list[str] = []
        self.len = 0
        self.max_len = max_len

    def ansi(self, code: str) -> None:
        self.parts.append(code)

    def text(self, text: str, width: int | None = None) -> None:
        width = len(text) if width is None else width
        room = self.max_len - self.len
        if room <= 0:
            return
        if width > room:
            text = text[:room]
            width = room
        self.parts.append(text)
        self.len += width

    def link(self, exercise: Exercise) -> None:
        if len(exercise.path) <= self.max_len - self.len:
            self.parts.append(exercise.link())
            self.len += len(exercise.path)
        else:
            self.text(exercise.path)

    def __str__(self) -> str:
        return "".join(self.parts)


class ListState:
    def __init__(self, app: AppState) -> None:
        self.app = app
        self.message = ""
        self.search_query = ""
        self.filter: str | None = None  # None, "done" or "pending"
        name_w = max([4] + [len(ex.name) for ex in app.exercises])
        path_w = max([4] + [len(ex.path) for ex in app.exercises])
        self.name_col_padding = " " * (name_w + COL_SPACING)
        self.path_col_padding = " " * path_w
        self.scroll = ScrollState(len(app.exercises), app.current_ind, 5)
        self.term_width = 0
        self.term_height = 0
        self.show_footer = True
        self.set_term_size(*term_size())

    def set_term_size(self, width: int, height: int) -> None:
        self.term_width, self.term_height = width, height
        if height == 0:
            return
        header_height, footer_height = 1, 3
        self.show_footer = height > header_height + footer_height
        self.scroll.set_max_n_rows_to_display(
            max(0, height - header_height - (footer_height if self.show_footer else 0))
        )

    # -- filtering ---------------------------------------------------------

    def filtered(self) -> list[tuple[int, Exercise]]:
        rows = list(enumerate(self.app.exercises))
        if self.filter == "done":
            return [(i, ex) for i, ex in rows if ex.done]
        if self.filter == "pending":
            return [(i, ex) for i, ex in rows if not ex.done]
        return rows

    def update_rows(self) -> None:
        self.scroll.set_n_rows(len(self.filtered()))

    def set_filter(self, value: str | None) -> None:
        self.filter = value
        self.update_rows()

    def toggle_filter(self, value: str) -> None:
        if self.filter == value:
            self.set_filter(None)
            self.message = f"Disabled filter {value.upper()}"
        else:
            self.set_filter(value)
            self.message = f"Enabled filter {value.upper()} │ Press {value[0]} again to disable the filter"

    def selected_exercise_ind(self) -> int | None:
        if self.scroll.selected is None:
            return None
        return self.filtered()[self.scroll.selected][0]

    # -- actions -----------------------------------------------------------

    def reset_selected(self) -> None:
        ind = self.selected_exercise_ind()
        if ind is None:
            self.message = "Nothing selected to reset!"
            return
        self.app.reset(ind)
        self.update_rows()
        self.message = f"The exercise `{self.app.exercises[ind].name}` has been reset"

    def apply_search_query(self) -> None:
        self.message = f"search:{self.search_query}|"
        if not self.search_query:
            return
        for pos, (_, ex) in enumerate(self.filtered()):
            if self.search_query in ex.name:
                self.scroll.set_selected(pos)
                return
        self.message += " (not found)"

    def selected_to_current(self) -> bool:
        ind = self.selected_exercise_ind()
        if ind is None:
            self.message = "Nothing selected to continue at!"
            return False
        self.app.set_current(ind)
        return True

    # -- drawing -----------------------------------------------------------

    def _draw_name(self, row: Row, ex: Exercise) -> None:
        q = self.search_query
        if q and (pos := ex.name.find(q)) != -1:
            row.text(ex.name[:pos])
            row.ansi(MAGENTA)
            row.text(q)
            row.ansi(FG_RESET)
            row.text(ex.name[pos + len(q) :])
        else:
            row.text(ex.name)

    def _draw_rows(self, lines: list[str]) -> int:
        offset = self.scroll.offset
        rows = self.filtered()[offset : offset + self.scroll.max_n_rows_to_display]
        for n, (ind, ex) in enumerate(rows):
            row = Row(self.term_width)
            if self.scroll.selected == offset + n:
                row.text(SNAKE, 2)
                row.ansi(REVERSE + BOLD)
            else:
                row.text("  ")
            if ind == self.app.current_ind:
                row.ansi(RED)
                row.text(">>>>>>>  ")
            else:
                row.text("         ")
            if ex.done:
                row.ansi(GREEN)
                row.text("DONE   ")
            else:
                row.ansi(YELLOW)
                row.text("PENDING")
            row.ansi(FG_RESET)
            row.text("  ")
            self._draw_name(row, ex)
            row.text(self.name_col_padding[len(ex.name) :])
            row.link(ex)
            row.text(self.path_col_padding[len(ex.path) :])
            row.ansi(RESET)
            lines.append(str(row))
        return len(rows)

    def _footer(self, lines: list[str]) -> None:
        lines.append(progress_bar(self.app.n_done, len(self.app.exercises), self.term_width))
        if self.message:
            lines.append(f"{MAGENTA}{self.message}{RESET}")
            lines.append("")
            return
        row = Row(self.term_width)
        if self.scroll.selected is not None:
            row.text("↓/j ↑/k home/g end/G | <c>ontinue at | <r>eset exercise")
            lines.append(str(row))
            row = Row(self.term_width)
            row.text("<s>earch | filter ")
        else:
            row.text("filter ")
        hl = f"{MAGENTA}{UNDERLINE}"
        if self.filter == "done":
            row.ansi(hl); row.text("<d>one"); row.ansi(RESET); row.text("/<p>ending")
        elif self.filter == "pending":
            row.text("<d>one/"); row.ansi(hl); row.text("<p>ending"); row.ansi(RESET)
        else:
            row.text("<d>one/<p>ending")
        row.text(" | <q>uit list")
        lines.append(str(row))

    def draw(self, out=sys.stdout) -> None:
        if self.term_height == 0:
            return
        lines: list[str] = []
        header = Row(self.term_width)
        header.text("  Current  State    Name")
        header.text(self.name_col_padding[4:])
        header.text("Path")
        lines.append(str(header))
        shown = self._draw_rows(lines)
        lines.extend([""] * (self.scroll.max_n_rows_to_display - shown))
        if self.show_footer:
            self._footer(lines)
        out.write("\x1b[?2026h" + move_to(0, 0))
        out.write((CLEAR_TO_EOL + "\r\n").join(lines) + CLEAR_TO_EOL)
        out.write("\x1b[?2026l")
        out.flush()


def list_mode(app: AppState, term: RawTerminal) -> None:
    out = sys.stdout
    out.write(ALT_SCREEN_ON + HIDE_CURSOR + "\x1b[?7l")  # no line wrap
    try:
        _handle_list(app, term)
    finally:
        out.write("\x1b[?7h" + SHOW_CURSOR + ALT_SCREEN_OFF)
        out.flush()


def _handle_list(app: AppState, term: RawTerminal) -> None:
    state = ListState(app)
    state.draw()
    searching = False
    while True:
        event = term.read_event(None)
        if isinstance(event, Resize):
            state.set_term_size(event.width, event.height)
            state.draw()
            continue
        if not isinstance(event, Key):
            continue
        state.message = ""

        if searching:
            match event.text:
                case "esc" | "enter":
                    searching = False
                    state.search_query = ""
                case "backspace":
                    state.search_query = state.search_query[:-1]
                    state.apply_search_query()
                case "ctrl-c":
                    return
                case text if text.isprintable():
                    state.search_query += text
                    state.apply_search_query()
                case _:
                    continue
            state.draw()
            continue

        match event.text:
            case "q" | "ctrl-c":
                return
            case "down" | "j":
                state.scroll.select_next()
            case "up" | "k":
                state.scroll.select_previous()
            case "home" | "g":
                state.scroll.select_first()
            case "end" | "G":
                state.scroll.select_last()
            case "d":
                state.toggle_filter("done")
            case "p":
                state.toggle_filter("pending")
            case "r":
                state.reset_selected()
            case "c":
                if state.selected_to_current():
                    return
            case "s" | "/":
                searching = True
                state.apply_search_query()
            case "esc":
                pass  # redraw to remove the message
            case _:
                continue
        state.draw()
