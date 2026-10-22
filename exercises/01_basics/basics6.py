# basics6.py
#
# Tuples are built by the comma, not by the parentheses. `return c, a, b`
# makes a 3-tuple. Assignment unpacks the same way, which is why swapping
# two variables in Python is just:
#
#     a, b = b, a
#
# No temporary variable, and the right-hand side is fully evaluated
# before anything is assigned.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def rotate(a: int, b: int, c: int) -> tuple[int, int, int]:
    # Move the last value to the front: (1, 2, 3) -> (3, 1, 2)
    return c, a, b


def swapped(pair: tuple[str, str]) -> tuple[str, str]:
    # Unpack the pair into two names, then return them the other way
    # round. Do it without indexing.
    a, b = pair

    return b, a


# --- checks (do not edit) ------------------------------------------
eq(rotate(1, 2, 3), (3, 1, 2))
eq(rotate(0, 0, 9), (9, 0, 0))
eq(swapped(("a", "b")), ("b", "a"))
eq(swapped(("only", "two")), ("two", "only"))
