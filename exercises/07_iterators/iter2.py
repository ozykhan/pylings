# iter2.py
#
# zip walks several iterables in step. By default it stops at the
# shortest one and says nothing, which quietly drops data.
#
# Since 3.10 you can pass strict=True to make a length mismatch raise
# instead. In production code that is almost always what you want --
# two sequences that should line up and do not is a bug, not a thing
# to silently trim.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, raises

def to_dict(keys: list[str], values: list[int]) -> dict[str, int]:
    # Pair them up. A length mismatch must raise, not truncate.
    return ...


# --- checks (do not edit) ------------------------------------------
eq(to_dict(["a", "b"], [1, 2]), {"a": 1, "b": 2})
eq(to_dict([], []), {})
raises(ValueError, lambda: to_dict(["a"], [1, 2]), "pass strict=True")
raises(ValueError, lambda: to_dict(["a", "b"], [1]))

# Demonstration of the default, so you know what you opted out of.
eq(list(zip([1, 2, 3], ["a"])), [(1, "a")], "two items vanished, silently")
