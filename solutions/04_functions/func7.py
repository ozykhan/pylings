# func7.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, raises

import functools

COMPUTED: list[int] = []


@functools.cache
def slow_square(n: int) -> int:
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
