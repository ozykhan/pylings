# typ3.py
#
# Containers are annotated with what they hold: list[str],
# dict[str, int], tuple[int, int], set[str].
#
# Since Python 3.9 you use the built-in names directly. If you see
# `from typing import List, Dict` in a tutorial, it is old -- those
# are deprecated aliases.
#
# For a parameter, prefer the most general type you actually need:
# Sequence[str] or Iterable[str] rather than list[str], so a caller
# can pass a tuple or a generator.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

def length_index(words):
    # TODO: annotate. It takes a list of strings and returns a dict
    # mapping each string to its length.
    return {word: len(word) for word in words}


# --- checks (do not edit) ------------------------------------------
from typing import get_type_hints

eq(length_index(["a", "bbb"]), {"a": 1, "bbb": 3})
eq(
    get_type_hints(length_index),
    {"words": list[str], "return": dict[str, int]},
    "use the built-in generics, not typing.List / typing.Dict",
)
