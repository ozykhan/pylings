# func3.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def tally(*numbers: int, start: int = 0) -> int:
    return start + sum(numbers)


def to_query(**params: str) -> str:
    return "&".join(f"{key}={value}" for key, value in params.items())


# --- checks (do not edit) ------------------------------------------
eq(tally(), 0)
eq(tally(1, 2, 3), 6)
eq(tally(1, 2, start=10), 13)
eq(tally(*[1, 2, 3]), 6, "a star at the call site spreads the list")

eq(to_query(), "")
eq(to_query(a="1"), "a=1")
eq(to_query(a="1", b="2"), "a=1&b=2")
eq(to_query(**{"q": "python", "page": "2"}), "q=python&page=2")
