# coll8.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

from collections import Counter, defaultdict


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    return Counter(text.lower().split()).most_common(n)


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    groups: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    return dict(groups)


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
