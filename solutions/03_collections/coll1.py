# coll1.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def collect(first: int, rest: list[int]) -> list[int]:
    return [first, *rest]


# --- checks (do not edit) ------------------------------------------
original = [2, 3]
eq(collect(1, original), [1, 2, 3])
eq(original, [2, 3], "rest must not be modified")
eq(collect(1, []), [1])

# Demonstration: append adds ONE item, extend adds each item.
xs = [1]
xs.append([2, 3])
eq(xs, [1, [2, 3]])
ys = [1]
ys.extend([2, 3])
eq(ys, [1, 2, 3])
