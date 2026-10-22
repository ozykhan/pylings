# coll7.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def leaderboard(rows: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(rows, key=lambda row: (-row[1], row[0]))


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
