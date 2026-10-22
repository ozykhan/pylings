# coll4.py
#
# Sets hold unique values and support the maths operators:
#
#     a | b   union
#     a & b   intersection
#     a - b   difference
#     a ^ b   in one or the other but not both
#
# Membership (`x in s`) is O(1) for a set and O(n) for a list. If you
# are calling `in` on a list inside a loop, you probably wanted a set.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

def unique_sorted(values: list[int]) -> list[int]:
    # Duplicates removed, ascending.
    return ...


def only_in_first(a: list[str], b: list[str]) -> set[str]:
    # Everything in a that is not in b.
    return ...


# --- checks (do not edit) ------------------------------------------
eq(unique_sorted([3, 1, 3, 2, 1]), [1, 2, 3])
eq(unique_sorted([]), [])
eq(unique_sorted([5]), [5])
eq(only_in_first(["a", "b", "c"], ["b"]), {"a", "c"})
eq(only_in_first(["a"], ["a"]), set())
eq(only_in_first([], ["a"]), set())
