# func5.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

from collections.abc import Callable


def make_multiplier(factor: int) -> Callable[[int], int]:
    def multiply(n: int) -> int:
        return n * factor

    return multiply


def make_counter() -> Callable[[], int]:
    count = 0

    def tick() -> int:
        nonlocal count
        count += 1
        return count

    return tick


# --- checks (do not edit) ------------------------------------------
double = make_multiplier(2)
triple = make_multiplier(3)
eq(double(5), 10)
eq(triple(5), 15)
eq(double(5), 10, "the closure keeps working")

counter = make_counter()
eq(counter(), 1)
eq(counter(), 2)
eq(counter(), 3)
eq(make_counter()(), 1, "a second counter starts from scratch")
