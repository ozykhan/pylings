# iter5.py
#
# itertools is a toolbox of lazy iterator functions. Two you will
# actually reach for:
#
#   chain.from_iterable(groups)   flattens one level
#   islice(iterable, n)           takes the first n, lazily
#
# islice works on infinite iterators, which a slice cannot do -- you
# cannot write `infinite[:5]`.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

from collections.abc import Iterable, Iterator
from itertools import chain, islice


def flatten(groups: list[list[int]]) -> list[int]:
    # [[1, 2], [3]] -> [1, 2, 3]
    return ...


def first_n(iterable: Iterable[int], n: int) -> list[int]:
    # The first n items. Must work on an infinite iterator.
    return ...


# --- checks (do not edit) ------------------------------------------
eq(flatten([[1, 2], [3]]), [1, 2, 3])
eq(flatten([]), [])
eq(flatten([[], [1]]), [1])

eq(first_n([1, 2, 3, 4], 2), [1, 2])
eq(first_n([1], 5), [1], "fewer items than asked for is fine")


def naturals() -> Iterator[int]:
    value = 0
    while True:
        value += 1
        yield value


eq(first_n(naturals(), 3), [1, 2, 3], "this must not hang")
