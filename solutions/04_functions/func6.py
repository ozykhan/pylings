# func6.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

import functools
from collections.abc import Callable
from typing import Any

CALLS: list[str] = []


def logged(fn: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        CALLS.append(fn.__name__)
        return fn(*args, **kwargs)

    return wrapper


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
