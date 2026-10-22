# err1.py
#
# Python leans on exceptions far more than JavaScript does. Iteration,
# attribute lookup and dict access are all built on them, and "try it
# and handle the failure" is idiomatic rather than sloppy.
#
# Catch the specific exception you expect. A bare `except:` also
# catches KeyboardInterrupt and SystemExit, which is how a program
# becomes impossible to stop.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

def safe_int(text: str, default: int = 0) -> int:
    # Parse text as an int. If it is not a number, return default.
    ...


# --- checks (do not edit) ------------------------------------------
eq(safe_int("12"), 12)
eq(safe_int("-3"), -3)
eq(safe_int("  7 "), 7, "int() ignores surrounding whitespace")
eq(safe_int("abc"), 0)
eq(safe_int(""), 0)
eq(safe_int("1.5"), 0, "int() will not parse a decimal point")
eq(safe_int("abc", -1), -1)
