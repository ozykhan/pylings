# coll4.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def unique_sorted(values: list[int]) -> list[int]:
    return sorted(set(values))


def only_in_first(a: list[str], b: list[str]) -> set[str]:
    return set(a) - set(b)


# --- checks (do not edit) ------------------------------------------
eq(unique_sorted([3, 1, 3, 2, 1]), [1, 2, 3])
eq(unique_sorted([]), [])
eq(unique_sorted([5]), [5])
eq(only_in_first(["a", "b", "c"], ["b"]), {"a", "c"})
eq(only_in_first(["a"], ["a"]), set())
eq(only_in_first([], ["a"]), set())
