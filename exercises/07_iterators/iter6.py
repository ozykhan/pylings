# iter6.py
#
# `for x in thing` works on anything with an __iter__ that returns an
# iterator. The simplest way to write one is to make __iter__ itself a
# generator -- put a yield in it and Python does the rest.
#
# An important difference: a generator is exhausted after one pass,
# but an object whose __iter__ builds a fresh generator each time can
# be looped over again and again. That is usually what you want from a
# collection.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

from collections.abc import Iterator


class Countdown:
    def __init__(self, start: int) -> None:
        self.start = start

    # TODO: make this iterable, counting down from start to 1.


# --- checks (do not edit) ------------------------------------------
c = Countdown(3)
eq(list(c), [3, 2, 1])
eq(list(c), [3, 2, 1], "it must be re-iterable, unlike a bare generator")
eq([n for n in Countdown(2)], [2, 1])
eq(list(Countdown(0)), [])
eq(max(Countdown(5)), 5, "anything that takes an iterable now works")
