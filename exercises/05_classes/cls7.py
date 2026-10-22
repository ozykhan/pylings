# cls7.py
#
# Inheritance, and super().
#
# super().__init__(...) calls the parent's initialiser. Forgetting it
# is the usual cause of "my attribute does not exist" in a subclass.
#
# Note that Shape.describe calls self.area(), and gets the subclass's
# version. That is ordinary dynamic dispatch, and it is most of what
# you actually need inheritance for.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, ok, raises

class Shape:
    def __init__(self, name: str) -> None:
        self.name = name

    def area(self) -> float:
        raise NotImplementedError

    def describe(self) -> str:
        return f"{self.name} with area {self.area()}"


class Rectangle(Shape):
    # TODO: __init__(self, width, height) -- remember super()
    # TODO: area()
    ...


# --- checks (do not edit) ------------------------------------------
r = Rectangle(3, 4)
eq(r.area(), 12)
eq(r.name, "rectangle", "did you call super().__init__?")
eq(r.describe(), "rectangle with area 12", "the parent method calls your area()")
ok(isinstance(r, Shape))
raises(NotImplementedError, lambda: Shape("blob").area())
