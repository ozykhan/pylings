# coll3.py
#
# `data[key]` raises KeyError when the key is missing. `data.get(key)`
# returns None instead, and `data.get(key, default)` returns whatever
# you pass.
#
# Use the subscript when a missing key is a bug, and .get when it is
# expected. Choosing deliberately is the point.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, raises


def count_or_default(data: dict[str, int], key: str) -> int:
    # The value at key, or 0 when it is not there. Must not raise.
    return data.get(key, 0)


def total(data: dict[str, int]) -> int:
    # The sum of every value.
    # total = 0
    # for value in data.values():
    #     total += value

    # return total

    return sum(data.values())


# --- checks (do not edit) ------------------------------------------
counts = {"a": 3, "b": 1}
eq(count_or_default(counts, "a"), 3)
eq(count_or_default(counts, "zzz"), 0)
eq(counts, {"a": 3, "b": 1}, "do not insert the missing key")
eq(total(counts), 4)
eq(total({}), 0)

# Demonstration: the subscript is the version that raises.
raises(KeyError, lambda: {}["missing"])
