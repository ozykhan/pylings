# coll3.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, raises

def count_or_default(data: dict[str, int], key: str) -> int:
    return data.get(key, 0)


def total(data: dict[str, int]) -> int:
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
