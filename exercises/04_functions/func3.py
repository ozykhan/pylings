# func3.py
#
# *args collects extra positional arguments into a tuple.
# **kwargs collects extra named arguments into a dict.
#
# The names are convention, the stars are the syntax. At a call site
# the same stars do the reverse: f(*items) spreads a list into
# positional arguments, f(**options) spreads a dict into named ones.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

def tally(*numbers: int, start: int = 0) -> int:
    # Add up every positional argument, beginning from start.
    return ...


def to_query(**params: str) -> str:
    # "a=1&b=2", in the order the arguments were given.
    return ...


# --- checks (do not edit) ------------------------------------------
eq(tally(), 0)
eq(tally(1, 2, 3), 6)
eq(tally(1, 2, start=10), 13)
eq(tally(*[1, 2, 3]), 6, "a star at the call site spreads the list")

eq(to_query(), "")
eq(to_query(a="1"), "a=1")
eq(to_query(a="1", b="2"), "a=1&b=2")
eq(to_query(**{"q": "python", "page": "2"}), "q=python&page=2")
