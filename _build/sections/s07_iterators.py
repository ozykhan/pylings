SECTION = "07_iterators"

EXERCISES = [
    dict(
        name="iter1",
        intro="""
        `for i in range(len(xs))` is a code smell in Python. When you need
        the index alongside the item, use enumerate -- and it takes a start
        argument, so human-facing numbering costs nothing.
        """,
        hint="""
        A comprehension over enumerate(lines, start=1), unpacking into two
        loop variables:
            [f"{i}. {line}" for i, line in enumerate(lines, start=1)]
        """,
        stub="""
        def numbered(lines: list[str]) -> list[str]:
            # ["a", "b"] -> ["1. a", "2. b"] -- numbering starts at 1.
            return ...
        """,
        solution="""
        def numbered(lines: list[str]) -> list[str]:
            return [f"{i}. {line}" for i, line in enumerate(lines, start=1)]
        """,
        checks="""
        eq(numbered(["a", "b"]), ["1. a", "2. b"])
        eq(numbered([]), [])
        eq(numbered(["only"]), ["1. only"])
        """,
    ),
    dict(
        name="iter2",
        intro="""
        zip walks several iterables in step. By default it stops at the
        shortest one and says nothing, which quietly drops data.

        Since 3.10 you can pass strict=True to make a length mismatch raise
        instead. In production code that is almost always what you want --
        two sequences that should line up and do not is a bug, not a thing
        to silently trim.
        """,
        hint="""
        dict() accepts an iterable of pairs, and zip produces exactly that:
            return dict(zip(keys, values, strict=True))
        """,
        stub="""
        def to_dict(keys: list[str], values: list[int]) -> dict[str, int]:
            # Pair them up. A length mismatch must raise, not truncate.
            return ...
        """,
        solution="""
        def to_dict(keys: list[str], values: list[int]) -> dict[str, int]:
            return dict(zip(keys, values, strict=True))
        """,
        checks="""
        eq(to_dict(["a", "b"], [1, 2]), {"a": 1, "b": 2})
        eq(to_dict([], []), {})
        raises(ValueError, lambda: to_dict(["a"], [1, 2]), "pass strict=True")
        raises(ValueError, lambda: to_dict(["a", "b"], [1]))

        # Demonstration of the default, so you know what you opted out of.
        eq(list(zip([1, 2, 3], ["a"])), [(1, "a")], "two items vanished, silently")
        """,
    ),
    dict(
        name="iter3",
        intro="""
        A function containing `yield` is a generator function. Calling it
        runs none of the body -- it returns a generator, and each `next()`
        runs until the following yield.

        This is how you process a million-line file in constant memory, and
        why building the whole list first is usually the wrong instinct.
        """,
        hint="""
        A while loop: while n > 0, yield n, then n -= 1. There is no return
        statement.
        """,
        stub="""
        from collections.abc import Iterator


        def countdown(n: int) -> Iterator[int]:
            # Yield n, n-1, ... down to 1. Nothing at or below zero.
            ...
        """,
        solution="""
        from collections.abc import Iterator


        def countdown(n: int) -> Iterator[int]:
            while n > 0:
                yield n
                n -= 1
        """,
        checks="""
        eq(list(countdown(3)), [3, 2, 1])
        eq(list(countdown(1)), [1])
        eq(list(countdown(0)), [])

        gen = countdown(2)
        not_ok(isinstance(gen, list), "a generator is not a list")
        eq(next(gen), 2)
        eq(next(gen), 1)
        raises(StopIteration, lambda: next(gen), "exhausted generators raise StopIteration")
        eq(list(countdown(2)), [2, 1], "but calling it again gives a fresh one")
        """,
    ),
    dict(
        name="iter4",
        intro="""
        A generator expression is a comprehension without the brackets. It
        produces items lazily, so when you are feeding a function that
        consumes an iterable -- sum, any, all, max, join -- you do not need
        to build a list first.

        any() and all() also short-circuit: any() stops at the first True.
        """,
        hint="""
        any_over: any(value > limit for value in values)
        total_length: sum(len(word) for word in words)
        No square brackets are needed inside the parentheses.
        """,
        stub="""
        def any_over(values: list[int], limit: int) -> bool:
            # True if at least one value is strictly greater than limit.
            return ...


        def total_length(words: list[str]) -> int:
            # The combined length of every word.
            return ...
        """,
        solution="""
        def any_over(values: list[int], limit: int) -> bool:
            return any(value > limit for value in values)


        def total_length(words: list[str]) -> int:
            return sum(len(word) for word in words)
        """,
        checks="""
        ok(any_over([1, 5, 2], 4))
        not_ok(any_over([1, 2], 4))
        not_ok(any_over([], 0), "any() of nothing is False")
        eq(total_length(["ab", "c"]), 3)
        eq(total_length([]), 0, "sum() of nothing is 0")

        # Demonstration: any() short-circuits, so the third item is never touched.
        seen: list[int] = []


        def watch(value: int) -> int:
            seen.append(value)
            return value


        any_over([watch(1), watch(9), 100], 5)
        eq(seen, [1, 9])
        """,
    ),
    dict(
        name="iter5",
        intro="""
        itertools is a toolbox of lazy iterator functions. Two you will
        actually reach for:

          chain.from_iterable(groups)   flattens one level
          islice(iterable, n)           takes the first n, lazily

        islice works on infinite iterators, which a slice cannot do -- you
        cannot write `infinite[:5]`.
        """,
        hint="""
        flatten: list(chain.from_iterable(groups))
        first_n: list(islice(iterable, n))
        """,
        stub="""
        from collections.abc import Iterable, Iterator
        from itertools import chain, islice


        def flatten(groups: list[list[int]]) -> list[int]:
            # [[1, 2], [3]] -> [1, 2, 3]
            return ...


        def first_n(iterable: Iterable[int], n: int) -> list[int]:
            # The first n items. Must work on an infinite iterator.
            return ...
        """,
        solution="""
        from collections.abc import Iterable, Iterator
        from itertools import chain, islice


        def flatten(groups: list[list[int]]) -> list[int]:
            return list(chain.from_iterable(groups))


        def first_n(iterable: Iterable[int], n: int) -> list[int]:
            return list(islice(iterable, n))
        """,
        checks="""
        eq(flatten([[1, 2], [3]]), [1, 2, 3])
        eq(flatten([]), [])
        eq(flatten([[], [1]]), [1])

        eq(first_n([1, 2, 3, 4], 2), [1, 2])
        eq(first_n([1], 5), [1], "fewer items than asked for is fine")


        def naturals() -> Iterator[int]:
            value = 0
            while True:
                value += 1
                yield value


        eq(first_n(naturals(), 3), [1, 2, 3], "this must not hang")
        """,
    ),
    dict(
        name="iter6",
        intro="""
        `for x in thing` works on anything with an __iter__ that returns an
        iterator. The simplest way to write one is to make __iter__ itself a
        generator -- put a yield in it and Python does the rest.

        An important difference: a generator is exhausted after one pass,
        but an object whose __iter__ builds a fresh generator each time can
        be looped over again and again. That is usually what you want from a
        collection.
        """,
        hint="""
        Make __iter__ a generator: a local `current = self.start`, then
        while current > 0: yield current; current -= 1.
        Do not store the counter on self, or the second loop will find it at
        zero.
        """,
        stub="""
        from collections.abc import Iterator


        class Countdown:
            def __init__(self, start: int) -> None:
                self.start = start

            # TODO: make this iterable, counting down from start to 1.
        """,
        solution="""
        from collections.abc import Iterator


        class Countdown:
            def __init__(self, start: int) -> None:
                self.start = start

            def __iter__(self) -> Iterator[int]:
                current = self.start
                while current > 0:
                    yield current
                    current -= 1
        """,
        checks="""
        c = Countdown(3)
        eq(list(c), [3, 2, 1])
        eq(list(c), [3, 2, 1], "it must be re-iterable, unlike a bare generator")
        eq([n for n in Countdown(2)], [2, 1])
        eq(list(Countdown(0)), [])
        eq(max(Countdown(5)), 5, "anything that takes an iterable now works")
        """,
    ),
]
