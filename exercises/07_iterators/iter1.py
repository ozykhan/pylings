# iter1.py
#
# `for i in range(len(xs))` is a code smell in Python. When you need
# the index alongside the item, use enumerate -- and it takes a start
# argument, so human-facing numbering costs nothing.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

def numbered(lines: list[str]) -> list[str]:
    # ["a", "b"] -> ["1. a", "2. b"] -- numbering starts at 1.
    return ...


# --- checks (do not edit) ------------------------------------------
eq(numbered(["a", "b"]), ["1. a", "2. b"])
eq(numbered([]), [])
eq(numbered(["only"]), ["1. only"])
