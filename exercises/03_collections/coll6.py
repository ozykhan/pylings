# coll6.py
#
# Comprehensions build dicts and sets too:
#
#     {k: v for ...}     dict comprehension
#     {v for ...}        set comprehension
#
# `data.items()` yields (key, value) pairs, which unpack straight into
# two loop variables.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def index_by_length(words: list[str]) -> dict[str, int]:
    # Each word mapped to its length.
    return {v: len(v) for v in words}


def invert(data: dict[str, int]) -> dict[int, str]:
    # Swap keys and values.

    return {v: k for k, v in data.items()}


# --- checks (do not edit) ------------------------------------------
eq(index_by_length(["a", "bbb"]), {"a": 1, "bbb": 3})
eq(index_by_length([]), {})
eq(index_by_length(["x", "x"]), {"x": 1}, "duplicate keys collapse")
eq(invert({"a": 1, "b": 2}), {1: "a", 2: "b"})
eq(invert({}), {})
