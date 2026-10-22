# cls2.py
#
# Two string conversions, for two audiences.
#
#   __repr__  for you: unambiguous, ideally valid Python. repr() and
#             the REPL and the contents of a printed list use it.
#   __str__   for users: readable. str(), print() and f-strings use it,
#             and fall back to __repr__ when __str__ is not defined.
#
# Always write __repr__. A debugging session against
# <__main__.Point object at 0x7f...> is wasted time.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...


# --- checks (do not edit) ------------------------------------------
p = Point(1, 2)
eq(repr(p), "Point(x=1, y=2)")
eq(str(p), "(1, 2)")
eq(f"{p}", "(1, 2)", "f-strings use __str__")
eq(f"{p!r}", "Point(x=1, y=2)", "!r forces __repr__")
eq(str([p]), "[Point(x=1, y=2)]", "containers show their items with repr")
