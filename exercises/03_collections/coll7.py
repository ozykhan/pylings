# coll7.py
#
# `sorted(iterable, key=...)` sorts by whatever the key function
# returns. Returning a tuple sorts by several fields at once.
#
# To mix directions -- descending on one field, ascending on another --
# negate the numeric one rather than using reverse=True, because
# reverse=True flips every field.
#
# Python's sort is stable, so equal keys keep their original order.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

def leaderboard(rows: list[tuple[str, int]]) -> list[tuple[str, int]]:
    # (name, score) rows, highest score first.
    # Ties broken by name, A to Z.
    return ...


# --- checks (do not edit) ------------------------------------------
eq(
    leaderboard([("bob", 5), ("ann", 9), ("cid", 5)]),
    [("ann", 9), ("bob", 5), ("cid", 5)],
)
eq(leaderboard([]), [])
eq(leaderboard([("z", 1), ("a", 1)]), [("a", 1), ("z", 1)])

rows = [("a", 1)]
leaderboard(rows)
eq(rows, [("a", 1)], "sorted() returns a new list; .sort() mutates in place")
