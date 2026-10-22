# iter4.py
#
# A generator expression is a comprehension without the brackets. It
# produces items lazily, so when you are feeding a function that
# consumes an iterable -- sum, any, all, max, join -- you do not need
# to build a list first.
#
# any() and all() also short-circuit: any() stops at the first True.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, ok, not_ok

def any_over(values: list[int], limit: int) -> bool:
    # True if at least one value is strictly greater than limit.
    return ...


def total_length(words: list[str]) -> int:
    # The combined length of every word.
    return ...


# --- checks (do not edit) ------------------------------------------
ok(any_over([1, 5, 2], 4))
not_ok(any_over([1, 2], 4))
not_ok(any_over([], 0), "any() of nothing is False")
eq(total_length(["ab", "c"]), 3)
eq(total_length([]), 0, "sum() of nothing is 0")

# Demonstration: any() short-circuits, so the third item is never touched.
seen: list[int] = []


def watch(value: int) -> int:
    seen.append(value)
    return value


any_over([watch(1), watch(9), 100], 5)
eq(seen, [1, 9])
