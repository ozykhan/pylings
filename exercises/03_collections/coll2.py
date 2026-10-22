# coll2.py
#
# Unpacking works on the left of an assignment too, and a starred name
# soaks up everything that is left over:
#
#     first, *rest = [1, 2, 3]      # first=1,  rest=[2, 3]
#     *body, last = [1, 2, 3]       # body=[1, 2], last=3
#
# The starred part is always a list, even when it ends up empty.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, raises


def head_tail(values: list[int]) -> tuple[int, list[int]]:
    # The first element, and everything after it as a list.
    # Use star unpacking, not indexing or slicing.
    first, *rest = values
    return (first, rest)


# --- checks (do not edit) ------------------------------------------
eq(head_tail([1, 2, 3]), (1, [2, 3]))
eq(head_tail([1]), (1, []), "the starred part is an empty list, not None")
eq(head_tail([9, 8]), (9, [8]))
raises(ValueError, lambda: head_tail([]), "unpacking an empty list must fail")
