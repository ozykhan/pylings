# basics1.py
#
# f-strings are Python's template literals. Where TypeScript writes
# `${expr}` inside backticks, Python writes {expr} inside a string
# prefixed with f.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def greet(name: str) -> str:
    return f"Hello, {name}!"


# --- checks (do not edit) ------------------------------------------
eq(greet("Faruk"), "Hello, Faruk!")
eq(greet("world"), "Hello, world!")
eq(greet(""), "Hello, !")
