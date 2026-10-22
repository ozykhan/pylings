# func6.py
#
# A decorator is a function that takes a function and returns a
# replacement. The @ syntax is only shorthand:
#
#     @logged
#     def work(): ...
#
#     # is exactly
#     work = logged(work)
#
# Always wrap the replacement with functools.wraps, or the decorated
# function loses its own __name__ and docstring -- which breaks
# tracebacks, debuggers and anything that introspects.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

import functools
from collections.abc import Callable
from typing import Any

CALLS: list[str] = []


def logged(fn: Callable[..., Any]) -> Callable[..., Any]:
    # Return a replacement that appends fn.__name__ to CALLS, then
    # calls fn with whatever arguments it was given and returns the
    # result unchanged.
    ...


# --- checks (do not edit) ------------------------------------------
@logged
def add(a: int, b: int = 0) -> int:
    "Adds two numbers."
    return a + b


eq(add(1, 2), 3, "the wrapper must return the real result")
eq(add(1, b=5), 6, "keyword arguments must pass through")
eq(CALLS, ["add", "add"])
eq(add.__name__, "add", "use functools.wraps to keep the name")
eq(add.__doc__, "Adds two numbers.", "and the docstring")
