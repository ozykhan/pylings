# basics4.py
#
# Python lets you chain comparisons the way maths does:
#
#     0 <= n <= 100
#
# means exactly what it looks like, and evaluates n only once. In
# TypeScript you would need `0 <= n && n <= 100`.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import ok, not_ok


def is_valid_status(code: int) -> bool:
    # An HTTP status code is anything from 100 to 599, inclusive.
    return 100 <= code <= 599


# --- checks (do not edit) ------------------------------------------
ok(is_valid_status(100))
ok(is_valid_status(200))
ok(is_valid_status(599))
not_ok(is_valid_status(99))
not_ok(is_valid_status(600))
not_ok(is_valid_status(0))
