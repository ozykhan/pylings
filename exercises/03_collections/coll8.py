# coll8.py
#
# The `collections` module has the containers you keep hand-rolling:
#
#   Counter      counts things, and .most_common(n) ranks them
#   defaultdict  a dict that creates a missing value instead of raising
#
# defaultdict(list) is the grouping idiom: groups[key].append(x) works
# even the first time a key is seen.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

from collections import Counter, defaultdict


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    # The n most common words, most common first.
    # Lowercase, split on whitespace.
    return ...


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    # {"a": ["ant", "ape"], ...}, preserving the input order.
    # Return a plain dict.
    return ...


# --- checks (do not edit) ------------------------------------------
eq(top_words("a b a c a b", 2), [("a", 3), ("b", 2)])
eq(top_words("Hello hello world", 1), [("hello", 2)])
eq(top_words("", 3), [])

eq(
    group_by_first_letter(["ant", "bee", "ape"]),
    {"a": ["ant", "ape"], "b": ["bee"]},
)
eq(group_by_first_letter([]), {})
eq(type(group_by_first_letter(["a"])), dict, "return a plain dict, not a defaultdict")
