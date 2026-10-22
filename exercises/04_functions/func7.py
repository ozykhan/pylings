# func7.py
#
# functools.cache memoizes a function: same arguments, same answer,
# computed once. It is one line and it is in the standard library.
#
# The arguments must be hashable, so this works for ints and strings
# and tuples, and not for lists or dicts. There is also
# functools.lru_cache(maxsize=N) when you need a bound on memory.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, raises

import functools

COMPUTED: list[int] = []


def slow_square(n: int) -> int:
    # TODO: memoize this so repeated arguments are computed once.
    COMPUTED.append(n)
    return n * n


# --- checks (do not edit) ------------------------------------------
eq(slow_square(3), 9)
eq(slow_square(3), 9)
eq(slow_square(3), 9)
eq(COMPUTED, [3], "computed once, then served from the cache")

eq(slow_square(4), 16)
eq(COMPUTED, [3, 4], "a new argument really is computed")

raises(TypeError, lambda: slow_square([1]), "cache keys must be hashable")
