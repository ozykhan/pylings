# coll2.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, raises

def head_tail(values: list[int]) -> tuple[int, list[int]]:
    first, *rest = values
    return first, rest


# --- checks (do not edit) ------------------------------------------
eq(head_tail([1, 2, 3]), (1, [2, 3]))
eq(head_tail([1]), (1, []), "the starred part is an empty list, not None")
eq(head_tail([9, 8]), (9, [8]))
raises(ValueError, lambda: head_tail([]), "unpacking an empty list must fail")
