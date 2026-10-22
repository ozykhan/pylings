# cls4.py
#
# @property turns a method into an attribute that is computed on
# access. This is why Python code has almost no getFoo()/setFoo()
# methods: you start with a plain attribute, and if it later needs
# logic you turn it into a property without changing a single caller.
#
# A matching @name.setter makes it assignable.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def fahrenheit(self) -> float:
        ...

    # TODO: add the setter, so `t.fahrenheit = 212` works.


# --- checks (do not edit) ------------------------------------------
t = Temperature(100)
eq(t.fahrenheit, 212.0, "accessed as an attribute, with no parentheses")

t.fahrenheit = 32
eq(t._celsius, 0.0, "the setter converts back")

frozen = Temperature(0)
eq(frozen.fahrenheit, 32.0)
