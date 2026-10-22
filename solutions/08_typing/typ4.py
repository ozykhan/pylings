# typ4.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def first(items: Sequence[T], default: T) -> T:
    for item in items:
        return item
    return default


# --- checks (do not edit) ------------------------------------------
eq(first([1, 2], 0), 1)
eq(first([], 99), 99)
eq(first("abc", "z"), "a", "a str is a Sequence too")
eq(first((), "fallback"), "fallback")
eq(first([None, 1], "x"), None, "the first item may itself be falsy")
