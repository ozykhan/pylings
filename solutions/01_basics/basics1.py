# basics1.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def greet(name: str) -> str:
    return f"Hello, {name}!"


# --- checks (do not edit) ------------------------------------------
eq(greet("Faruk"), "Hello, Faruk!")
eq(greet("world"), "Hello, world!")
eq(greet(""), "Hello, !")
