# func2.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def add_item(item: str, basket: list[str] | None = None) -> list[str]:
    if basket is None:
        basket = []
    basket.append(item)
    return basket


# --- checks (do not edit) ------------------------------------------
eq(add_item("a"), ["a"])
eq(add_item("b"), ["b"], "a fresh list each call -- not ['a', 'b']")
eq(add_item("c"), ["c"])

mine = ["x"]
eq(add_item("y", mine), ["x", "y"])
eq(mine, ["x", "y"], "a basket that was passed in is appended to in place")

# Demonstration of the bug, so you have seen it happen.
def broken(item, basket=[]):
    basket.append(item)
    return basket

eq(broken(1), [1])
eq(broken(2), [1, 2], "the default list survived between calls")
