# basics4.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import ok, not_ok

def is_valid_status(code: int) -> bool:
    return 100 <= code <= 599


# --- checks (do not edit) ------------------------------------------
ok(is_valid_status(100))
ok(is_valid_status(200))
ok(is_valid_status(599))
not_ok(is_valid_status(99))
not_ok(is_valid_status(600))
not_ok(is_valid_status(0))
