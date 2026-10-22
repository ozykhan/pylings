# cls4.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self._celsius = (value - 32) * 5 / 9


# --- checks (do not edit) ------------------------------------------
t = Temperature(100)
eq(t.fahrenheit, 212.0, "accessed as an attribute, with no parentheses")

t.fahrenheit = 32
eq(t._celsius, 0.0, "the setter converts back")

frozen = Temperature(0)
eq(frozen.fahrenheit, 32.0)
