# cls1.py
#
# A class body defines methods; `__init__` sets up a new instance.
# Every method takes the instance as its first parameter, and by
# convention it is called `self`. It is explicit -- there is no
# implicit `this`, and no way to lose the binding.
#
# Attributes are created by assigning to self.something. There is no
# separate declaration step.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

class Counter:
    def __init__(self, start: int = 0) -> None:
        ...

    def increment(self, by: int = 1) -> None:
        ...


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
