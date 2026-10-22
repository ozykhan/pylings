# func2.py
#
# THE Python gotcha. A default argument is evaluated ONCE, when the
# function is defined -- not on each call. So this is broken:
#
#     def add(item, basket=[]):   # the SAME list every call
#         basket.append(item)
#         return basket
#
# Call it twice and the second call still has the first item in it.
# The fix is always the same: default to None and build the real value
# inside the body.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

def add_item(item: str, basket: list[str] | None = None) -> list[str]:
    # Append item to basket and return it.
    # When no basket is given, start a FRESH empty one each call.
    ...


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
