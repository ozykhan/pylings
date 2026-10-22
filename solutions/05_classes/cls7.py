# cls7.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, ok, raises

class Shape:
    def __init__(self, name: str) -> None:
        self.name = name

    def area(self) -> float:
        raise NotImplementedError

    def describe(self) -> str:
        return f"{self.name} with area {self.area()}"


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


# --- checks (do not edit) ------------------------------------------
r = Rectangle(3, 4)
eq(r.area(), 12)
eq(r.name, "rectangle", "did you call super().__init__?")
eq(r.describe(), "rectangle with area 12", "the parent method calls your area()")
ok(isinstance(r, Shape))
raises(NotImplementedError, lambda: Shape("blob").area())
