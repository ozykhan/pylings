# typ3.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def length_index(words: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words}


# --- checks (do not edit) ------------------------------------------
from typing import get_type_hints

eq(length_index(["a", "bbb"]), {"a": 1, "bbb": 3})
eq(
    get_type_hints(length_index),
    {"words": list[str], "return": dict[str, int]},
    "use the built-in generics, not typing.List / typing.Dict",
)
