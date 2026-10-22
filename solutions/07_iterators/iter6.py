# iter6.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

from collections.abc import Iterator


class Countdown:
    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self) -> Iterator[int]:
        current = self.start
        while current > 0:
            yield current
            current -= 1


# --- checks (do not edit) ------------------------------------------
c = Countdown(3)
eq(list(c), [3, 2, 1])
eq(list(c), [3, 2, 1], "it must be re-iterable, unlike a bare generator")
eq([n for n in Countdown(2)], [2, 1])
eq(list(Countdown(0)), [])
eq(max(Countdown(5)), 5, "anything that takes an iterable now works")
