SECTION = "03_collections"

EXERCISES = [
    dict(
        name="coll1",
        intro="""
        Four built-in containers you will use constantly:
          list  [1, 2]     ordered, mutable
          tuple (1, 2)     ordered, immutable, hashable
          dict  {"a": 1}   key -> value, insertion-ordered since 3.7
          set   {1, 2}     unordered, unique, fast membership tests

        Inside a list literal, a * unpacks another iterable into it. That is
        the same idea as JavaScript's spread.
        """,
        hint="""
        Build a new list literal with the single value first and the rest
        spread into it:
            return [first, *rest]
        """,
        stub="""
        def collect(first: int, rest: list[int]) -> list[int]:
            # A NEW list: first, then everything in rest.
            # Do not modify rest.
            return ...
        """,
        solution="""
        def collect(first: int, rest: list[int]) -> list[int]:
            return [first, *rest]
        """,
        checks="""
        original = [2, 3]
        eq(collect(1, original), [1, 2, 3])
        eq(original, [2, 3], "rest must not be modified")
        eq(collect(1, []), [1])

        # Demonstration: append adds ONE item, extend adds each item.
        xs = [1]
        xs.append([2, 3])
        eq(xs, [1, [2, 3]])
        ys = [1]
        ys.extend([2, 3])
        eq(ys, [1, 2, 3])
        """,
    ),
    dict(
        name="coll2",
        intro="""
        Unpacking works on the left of an assignment too, and a starred name
        soaks up everything that is left over:

            first, *rest = [1, 2, 3]      # first=1,  rest=[2, 3]
            *body, last = [1, 2, 3]       # body=[1, 2], last=3

        The starred part is always a list, even when it ends up empty.
        """,
        hint="""
        Two statements. Unpack with a star, then return the pair:
            first, *rest = values
            return first, rest
        """,
        stub="""
        def head_tail(values: list[int]) -> tuple[int, list[int]]:
            # The first element, and everything after it as a list.
            # Use star unpacking, not indexing or slicing.
            ...
        """,
        solution="""
        def head_tail(values: list[int]) -> tuple[int, list[int]]:
            first, *rest = values
            return first, rest
        """,
        checks="""
        eq(head_tail([1, 2, 3]), (1, [2, 3]))
        eq(head_tail([1]), (1, []), "the starred part is an empty list, not None")
        eq(head_tail([9, 8]), (9, [8]))
        raises(ValueError, lambda: head_tail([]), "unpacking an empty list must fail")
        """,
    ),
    dict(
        name="coll3",
        intro="""
        `data[key]` raises KeyError when the key is missing. `data.get(key)`
        returns None instead, and `data.get(key, default)` returns whatever
        you pass.

        Use the subscript when a missing key is a bug, and .get when it is
        expected. Choosing deliberately is the point.
        """,
        hint="""
        count_or_default is one call to .get with a second argument.
        total is sum() over data.values().
        """,
        stub="""
        def count_or_default(data: dict[str, int], key: str) -> int:
            # The value at key, or 0 when it is not there. Must not raise.
            return ...


        def total(data: dict[str, int]) -> int:
            # The sum of every value.
            return ...
        """,
        solution="""
        def count_or_default(data: dict[str, int], key: str) -> int:
            return data.get(key, 0)


        def total(data: dict[str, int]) -> int:
            return sum(data.values())
        """,
        checks="""
        counts = {"a": 3, "b": 1}
        eq(count_or_default(counts, "a"), 3)
        eq(count_or_default(counts, "zzz"), 0)
        eq(counts, {"a": 3, "b": 1}, "do not insert the missing key")
        eq(total(counts), 4)
        eq(total({}), 0)

        # Demonstration: the subscript is the version that raises.
        raises(KeyError, lambda: {}["missing"])
        """,
    ),
    dict(
        name="coll4",
        intro="""
        Sets hold unique values and support the maths operators:

            a | b   union
            a & b   intersection
            a - b   difference
            a ^ b   in one or the other but not both

        Membership (`x in s`) is O(1) for a set and O(n) for a list. If you
        are calling `in` on a list inside a loop, you probably wanted a set.
        """,
        hint="""
        unique_sorted: sorted() accepts any iterable and always returns a
        list, so sorted(set(values)) does both jobs at once.
        only_in_first: convert both to sets and subtract.
        """,
        stub="""
        def unique_sorted(values: list[int]) -> list[int]:
            # Duplicates removed, ascending.
            return ...


        def only_in_first(a: list[str], b: list[str]) -> set[str]:
            # Everything in a that is not in b.
            return ...
        """,
        solution="""
        def unique_sorted(values: list[int]) -> list[int]:
            return sorted(set(values))


        def only_in_first(a: list[str], b: list[str]) -> set[str]:
            return set(a) - set(b)
        """,
        checks="""
        eq(unique_sorted([3, 1, 3, 2, 1]), [1, 2, 3])
        eq(unique_sorted([]), [])
        eq(unique_sorted([5]), [5])
        eq(only_in_first(["a", "b", "c"], ["b"]), {"a", "c"})
        eq(only_in_first(["a"], ["a"]), set())
        eq(only_in_first([], ["a"]), set())
        """,
    ),
    dict(
        name="coll5",
        intro="""
        A list comprehension is filter + map in one expression:

            [expression for item in iterable if condition]

        It is the idiomatic way to build a list. Reach for it before you
        reach for a for-loop with .append(), and before map/filter -- which
        exist in Python but are rarely the clearest choice.
        """,
        hint="""
        One comprehension with both a transform and a filter:
            [v * v for v in values if v % 2 == 0]
        """,
        stub="""
        def squares_of_evens(values: list[int]) -> list[int]:
            # Square each even number, keep the original order.
            # Use a comprehension.
            return ...
        """,
        solution="""
        def squares_of_evens(values: list[int]) -> list[int]:
            return [v * v for v in values if v % 2 == 0]
        """,
        checks="""
        eq(squares_of_evens([1, 2, 3, 4]), [4, 16])
        eq(squares_of_evens([]), [])
        eq(squares_of_evens([1, 3, 5]), [])
        eq(squares_of_evens([0, -2]), [0, 4])
        """,
    ),
    dict(
        name="coll6",
        intro="""
        Comprehensions build dicts and sets too:

            {k: v for ...}     dict comprehension
            {v for ...}        set comprehension

        `data.items()` yields (key, value) pairs, which unpack straight into
        two loop variables.
        """,
        hint="""
        index_by_length: {word: len(word) for word in words}
        invert: loop over data.items() and put the value first.
        """,
        stub="""
        def index_by_length(words: list[str]) -> dict[str, int]:
            # Each word mapped to its length.
            return ...


        def invert(data: dict[str, int]) -> dict[int, str]:
            # Swap keys and values.
            return ...
        """,
        solution="""
        def index_by_length(words: list[str]) -> dict[str, int]:
            return {word: len(word) for word in words}


        def invert(data: dict[str, int]) -> dict[int, str]:
            return {value: key for key, value in data.items()}
        """,
        checks="""
        eq(index_by_length(["a", "bbb"]), {"a": 1, "bbb": 3})
        eq(index_by_length([]), {})
        eq(index_by_length(["x", "x"]), {"x": 1}, "duplicate keys collapse")
        eq(invert({"a": 1, "b": 2}), {1: "a", 2: "b"})
        eq(invert({}), {})
        """,
    ),
    dict(
        name="coll7",
        intro="""
        `sorted(iterable, key=...)` sorts by whatever the key function
        returns. Returning a tuple sorts by several fields at once.

        To mix directions -- descending on one field, ascending on another --
        negate the numeric one rather than using reverse=True, because
        reverse=True flips every field.

        Python's sort is stable, so equal keys keep their original order.
        """,
        hint="""
        The key returns a tuple. Negate the score so bigger scores sort
        first, and leave the name as-is so it sorts A to Z:
            key=lambda row: (-row[1], row[0])
        """,
        stub="""
        def leaderboard(rows: list[tuple[str, int]]) -> list[tuple[str, int]]:
            # (name, score) rows, highest score first.
            # Ties broken by name, A to Z.
            return ...
        """,
        solution="""
        def leaderboard(rows: list[tuple[str, int]]) -> list[tuple[str, int]]:
            return sorted(rows, key=lambda row: (-row[1], row[0]))
        """,
        checks="""
        eq(
            leaderboard([("bob", 5), ("ann", 9), ("cid", 5)]),
            [("ann", 9), ("bob", 5), ("cid", 5)],
        )
        eq(leaderboard([]), [])
        eq(leaderboard([("z", 1), ("a", 1)]), [("a", 1), ("z", 1)])

        rows = [("a", 1)]
        leaderboard(rows)
        eq(rows, [("a", 1)], "sorted() returns a new list; .sort() mutates in place")
        """,
    ),
    dict(
        name="coll8",
        intro="""
        The `collections` module has the containers you keep hand-rolling:

          Counter      counts things, and .most_common(n) ranks them
          defaultdict  a dict that creates a missing value instead of raising

        defaultdict(list) is the grouping idiom: groups[key].append(x) works
        even the first time a key is seen.
        """,
        hint="""
        top_words: Counter(text.lower().split()).most_common(n)
        group_by_first_letter: make a defaultdict(list), loop and append,
        then wrap it in dict(...) before returning so the caller gets a
        plain dict.
        """,
        stub="""
        from collections import Counter, defaultdict


        def top_words(text: str, n: int) -> list[tuple[str, int]]:
            # The n most common words, most common first.
            # Lowercase, split on whitespace.
            return ...


        def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
            # {"a": ["ant", "ape"], ...}, preserving the input order.
            # Return a plain dict.
            return ...
        """,
        solution="""
        from collections import Counter, defaultdict


        def top_words(text: str, n: int) -> list[tuple[str, int]]:
            return Counter(text.lower().split()).most_common(n)


        def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
            groups: defaultdict[str, list[str]] = defaultdict(list)
            for word in words:
                groups[word[0]].append(word)
            return dict(groups)
        """,
        checks="""
        eq(top_words("a b a c a b", 2), [("a", 3), ("b", 2)])
        eq(top_words("Hello hello world", 1), [("hello", 2)])
        eq(top_words("", 3), [])

        eq(
            group_by_first_letter(["ant", "bee", "ape"]),
            {"a": ["ant", "ape"], "b": ["bee"]},
        )
        eq(group_by_first_letter([]), {})
        eq(type(group_by_first_letter(["a"])), dict, "return a plain dict, not a defaultdict")
        """,
    ),
]
