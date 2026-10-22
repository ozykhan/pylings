# coll6.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def index_by_length(words: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words}


def invert(data: dict[str, int]) -> dict[int, str]:
    return {value: key for key, value in data.items()}


# --- checks (do not edit) ------------------------------------------
eq(index_by_length(["a", "bbb"]), {"a": 1, "bbb": 3})
eq(index_by_length([]), {})
eq(index_by_length(["x", "x"]), {"x": 1}, "duplicate keys collapse")
eq(invert({"a": 1, "b": 2}), {1: "a", 2: "b"})
eq(invert({}), {})
