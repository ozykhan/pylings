# iter1.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def numbered(lines: list[str]) -> list[str]:
    return [f"{i}. {line}" for i, line in enumerate(lines, start=1)]


# --- checks (do not edit) ------------------------------------------
eq(numbered(["a", "b"]), ["1. a", "2. b"])
eq(numbered([]), [])
eq(numbered(["only"]), ["1. only"])
