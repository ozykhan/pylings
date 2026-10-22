# typ4.py
#
# A TypeVar links types together. `def first(items: Sequence[T],
# default: T) -> T` says: whatever the sequence holds, the default and
# the result are that same type. Annotating it as `object` would lose
# exactly that.
#
# Python 3.12 added a shorter spelling -- `def first[T](...)` -- with
# no TypeVar declaration. The explicit form here still works
# everywhere and is what you will meet in existing code.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def first(items: Sequence[T], default: T) -> T:
    # The first item, or default when there are none.
    ...


# --- checks (do not edit) ------------------------------------------
eq(first([1, 2], 0), 1)
eq(first([], 99), 99)
eq(first("abc", "z"), "a", "a str is a Sequence too")
eq(first((), "fallback"), "fallback")
eq(first([None, 1], "x"), None, "the first item may itself be falsy")
