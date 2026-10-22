# basics6.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def rotate(a: int, b: int, c: int) -> tuple[int, int, int]:
    return c, a, b


def swapped(pair: tuple[str, str]) -> tuple[str, str]:
    left, right = pair
    return right, left


# --- checks (do not edit) ------------------------------------------
eq(rotate(1, 2, 3), (3, 1, 2))
eq(rotate(0, 0, 9), (9, 0, 0))
eq(swapped(("a", "b")), ("b", "a"))
eq(swapped(("only", "two")), ("two", "only"))
