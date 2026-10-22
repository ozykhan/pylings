# cls2.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


# --- checks (do not edit) ------------------------------------------
p = Point(1, 2)
eq(repr(p), "Point(x=1, y=2)")
eq(str(p), "(1, 2)")
eq(f"{p}", "(1, 2)", "f-strings use __str__")
eq(f"{p!r}", "Point(x=1, y=2)", "!r forces __repr__")
eq(str([p]), "[Point(x=1, y=2)]", "containers show their items with repr")
