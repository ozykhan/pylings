# func5.py
#
# Functions are objects. You can define one inside another, return it,
# and it keeps a reference to the enclosing scope. That is a closure --
# exactly as in JavaScript.
#
# One difference: assigning to a name inside a function makes it local
# by default. To assign to a name from the enclosing function you must
# say `nonlocal` first. (`global` is the module-level equivalent, and
# you should almost never need it.)
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from collections.abc import Callable

from pylings_check import eq


def make_multiplier(factor: int) -> Callable[[int], int]:
    # Return a function that multiplies its argument by factor.
    def multiply_by_factor(n: int) -> int:
        return n * factor

    return multiply_by_factor


def make_counter() -> Callable[[], int]:
    # Return a function that returns 1, then 2, then 3, ...
    # Each counter made here is independent.
    x = 0

    def counter() -> int:
        nonlocal x
        x += 1
        return x

    return counter


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
