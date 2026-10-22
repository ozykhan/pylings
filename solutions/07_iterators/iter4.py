# iter4.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, ok, not_ok

def any_over(values: list[int], limit: int) -> bool:
    return any(value > limit for value in values)


def total_length(words: list[str]) -> int:
    return sum(len(word) for word in words)


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
