# coll5.py
#
# A list comprehension is filter + map in one expression:
#
#     [expression for item in iterable if condition]
#
# It is the idiomatic way to build a list. Reach for it before you
# reach for a for-loop with .append(), and before map/filter -- which
# exist in Python but are rarely the clearest choice.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def squares_of_evens(values: list[int]) -> list[int]:
    # Square each even number, keep the original order.
    # Use a comprehension.

    return [v * v for v in values if v % 2 == 0]


# --- checks (do not edit) ------------------------------------------
eq(squares_of_evens([1, 2, 3, 4]), [4, 16])
eq(squares_of_evens([]), [])
eq(squares_of_evens([1, 3, 5]), [])
eq(squares_of_evens([0, -2]), [0, 4])
