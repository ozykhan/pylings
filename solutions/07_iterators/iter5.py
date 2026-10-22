# iter5.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

from collections.abc import Iterable, Iterator
from itertools import chain, islice


def flatten(groups: list[list[int]]) -> list[int]:
    return list(chain.from_iterable(groups))


def first_n(iterable: Iterable[int], n: int) -> list[int]:
    return list(islice(iterable, n))


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
