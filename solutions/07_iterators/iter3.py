# iter3.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, ok, not_ok, raises

from collections.abc import Iterator


def countdown(n: int) -> Iterator[int]:
    while n > 0:
        yield n
        n -= 1


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
