# err1.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def safe_int(text: str, default: int = 0) -> int:
    try:
        return int(text)
    except ValueError:
        return default


# --- checks (do not edit) ------------------------------------------
eq(safe_int("12"), 12)
eq(safe_int("-3"), -3)
eq(safe_int("  7 "), 7, "int() ignores surrounding whitespace")
eq(safe_int("abc"), 0)
eq(safe_int(""), 0)
eq(safe_int("1.5"), 0, "int() will not parse a decimal point")
eq(safe_int("abc", -1), -1)
