# iter3.py
#
# A function containing `yield` is a generator function. Calling it
# runs none of the body -- it returns a generator, and each `next()`
# runs until the following yield.
#
# This is how you process a million-line file in constant memory, and
# why building the whole list first is usually the wrong instinct.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, ok, not_ok, raises

from collections.abc import Iterator


def countdown(n: int) -> Iterator[int]:
    # Yield n, n-1, ... down to 1. Nothing at or below zero.
    ...


# --- checks (do not edit) ------------------------------------------
eq(list(countdown(3)), [3, 2, 1])
eq(list(countdown(1)), [1])
eq(list(countdown(0)), [])

gen = countdown(2)
not_ok(isinstance(gen, list), "a generator is not a list")
eq(next(gen), 2)
eq(next(gen), 1)
raises(StopIteration, lambda: next(gen), "exhausted generators raise StopIteration")
eq(list(countdown(2)), [2, 1], "but calling it again gives a fresh one")
