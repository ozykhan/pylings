# iter2.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, raises

def to_dict(keys: list[str], values: list[int]) -> dict[str, int]:
    return dict(zip(keys, values, strict=True))


# --- checks (do not edit) ------------------------------------------
eq(to_dict(["a", "b"], [1, 2]), {"a": 1, "b": 2})
eq(to_dict([], []), {})
raises(ValueError, lambda: to_dict(["a"], [1, 2]), "pass strict=True")
raises(ValueError, lambda: to_dict(["a", "b"], [1]))

# Demonstration of the default, so you know what you opted out of.
eq(list(zip([1, 2, 3], ["a"])), [(1, "a")], "two items vanished, silently")
