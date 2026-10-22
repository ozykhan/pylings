# cls1.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

class Counter:
    def __init__(self, start: int = 0) -> None:
        self.value = start

    def increment(self, by: int = 1) -> None:
        self.value += by


# --- checks (do not edit) ------------------------------------------
c = Counter()
eq(c.value, 0)
c.increment()
eq(c.value, 1)
c.increment(10)
eq(c.value, 11)

other = Counter(100)
eq(other.value, 100)
eq(c.value, 11, "instances do not share state")
