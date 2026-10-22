# coll1.py
#
# Four built-in containers you will use constantly:
#   list  [1, 2]     ordered, mutable
#   tuple (1, 2)     ordered, immutable, hashable
#   dict  {"a": 1}   key -> value, insertion-ordered since 3.7
#   set   {1, 2}     unordered, unique, fast membership tests
#
# Inside a list literal, a * unpacks another iterable into it. That is
# the same idea as JavaScript's spread.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def collect(first: int, rest: list[int]) -> list[int]:
    # A NEW list: first, then everything in rest.
    # Do not modify rest.

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
