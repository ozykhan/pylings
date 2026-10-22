SECTION = "01_basics"

EXERCISES = [
    dict(
        name="basics1",
        intro="""
        f-strings are Python's template literals. Where TypeScript writes
        `${expr}` inside backticks, Python writes {expr} inside a string
        prefixed with f.
        """,
        hint="""
        Put an f directly before the opening quote, and the variable in braces:
            f"Hello, {name}!"
        Without the f prefix you get the literal text {name}.
        """,
        stub="""
        def greet(name: str) -> str:
            return ...
        """,
        solution="""
        def greet(name: str) -> str:
            return f"Hello, {name}!"
        """,
        checks="""
        eq(greet("Faruk"), "Hello, Faruk!")
        eq(greet("world"), "Hello, world!")
        eq(greet(""), "Hello, !")
        """,
    ),
    dict(
        name="basics2",
        intro="""
        Every Python object is either truthy or falsy. The falsy ones are:
        False, None, 0, 0.0, "" and every empty container -- [], {}, set(),
        (). Everything else is truthy.

        This is why `if items:` is the idiomatic way to ask "is this list
        non-empty", rather than `if len(items) > 0`.
        """,
        hint="""
        `not value` turns any object into a bool: True when the object is
        falsy, False when it is truthy. That is the whole exercise.
        """,
        stub="""
        def is_blank(value: object) -> bool:
            return ...
        """,
        solution="""
        def is_blank(value: object) -> bool:
            return not value
        """,
        checks="""
        eq(is_blank(""), True, "return a real bool, not just something truthy")
        ok(is_blank(""), "empty string is falsy")
        ok(is_blank([]), "empty list is falsy")
        ok(is_blank({}), "empty dict is falsy")
        ok(is_blank(set()), "empty set is falsy")
        ok(is_blank(0), "zero is falsy")
        ok(is_blank(None), "None is falsy")
        not_ok(is_blank("x"))
        not_ok(is_blank([0]), "a list holding a falsy value is still non-empty")
        not_ok(is_blank(0.5))
        """,
    ),
    dict(
        name="basics3",
        intro="""
        Now the trap that follows from basics2.

        `if not port:` is True for None *and* for 0. If 0 is a legitimate
        value, that check silently throws it away. The fix is to ask the
        question you actually mean: `if port is None:`.

        This is the single most common bug when people carry JavaScript
        habits over -- it is the same class of mistake as using || instead
        of ?? for defaults.
        """,
        hint="""
        Use `is None`, not truthiness. A conditional expression reads well
        here:
            return X if port is None else port
        """,
        stub="""
        def resolve_port(port: int | None) -> int:
            # Return 8080 when no port was given.
            # But 0 is a real value a caller might pass, so keep it.
            return ...
        """,
        solution="""
        def resolve_port(port: int | None) -> int:
            return 8080 if port is None else port
        """,
        checks="""
        eq(resolve_port(None), 8080, "no port given -> the default")
        eq(resolve_port(0), 0, "0 was given explicitly -- do not replace it")
        eq(resolve_port(3000), 3000)
        """,
    ),
    dict(
        name="basics4",
        intro="""
        Python lets you chain comparisons the way maths does:

            0 <= n <= 100

        means exactly what it looks like, and evaluates n only once. In
        TypeScript you would need `0 <= n && n <= 100`.
        """,
        hint="""
        One chained comparison is enough:
            return 100 <= code <= 599
        """,
        stub="""
        def is_valid_status(code: int) -> bool:
            # An HTTP status code is anything from 100 to 599, inclusive.
            return ...
        """,
        solution="""
        def is_valid_status(code: int) -> bool:
            return 100 <= code <= 599
        """,
        checks="""
        ok(is_valid_status(100))
        ok(is_valid_status(200))
        ok(is_valid_status(599))
        not_ok(is_valid_status(99))
        not_ok(is_valid_status(600))
        not_ok(is_valid_status(0))
        """,
    ),
    dict(
        name="basics5",
        intro="""
        Integer maths. `/` always gives a float. `//` is floor division and
        `%` is the remainder that goes with it.

        Careful: Python floors toward negative infinity, JavaScript truncates
        toward zero. So -7 // 2 is -4 in Python and -3 in JS, and -7 % 2 is 1
        in Python and -1 in JS. Python's version is the one that makes clock
        arithmetic work.

        `divmod(a, b)` gives you both results at once as a tuple.
        """,
        hint="""
        divmod(total, 60) already returns exactly the (minutes, seconds)
        tuple you need. One line.
        """,
        stub="""
        def split_seconds(total: int) -> tuple[int, int]:
            # Turn a number of seconds into (minutes, seconds).
            return ...
        """,
        solution="""
        def split_seconds(total: int) -> tuple[int, int]:
            return divmod(total, 60)
        """,
        checks="""
        eq(split_seconds(0), (0, 0))
        eq(split_seconds(59), (0, 59))
        eq(split_seconds(60), (1, 0))
        eq(split_seconds(125), (2, 5))
        eq(split_seconds(3600), (60, 0))

        # Demonstrations, not tasks -- these already pass. Read them.
        eq(7 / 2, 3.5, "/ always produces a float")
        eq(7 // 2, 3, "// floors")
        eq(-7 // 2, -4, "floors toward negative infinity, unlike JavaScript")
        eq(-7 % 2, 1, "the remainder follows the same convention")
        """,
    ),
    dict(
        name="basics6",
        intro="""
        Tuples are built by the comma, not by the parentheses. `return c, a, b`
        makes a 3-tuple. Assignment unpacks the same way, which is why swapping
        two variables in Python is just:

            a, b = b, a

        No temporary variable, and the right-hand side is fully evaluated
        before anything is assigned.
        """,
        hint="""
        You do not need parentheses or a temporary variable. The whole body of
        each function is a single line built from commas.
        """,
        stub="""
        def rotate(a: int, b: int, c: int) -> tuple[int, int, int]:
            # Move the last value to the front: (1, 2, 3) -> (3, 1, 2)
            return ...


        def swapped(pair: tuple[str, str]) -> tuple[str, str]:
            # Unpack the pair into two names, then return them the other way
            # round. Do it without indexing.
            ...
        """,
        solution="""
        def rotate(a: int, b: int, c: int) -> tuple[int, int, int]:
            return c, a, b


        def swapped(pair: tuple[str, str]) -> tuple[str, str]:
            left, right = pair
            return right, left
        """,
        checks="""
        eq(rotate(1, 2, 3), (3, 1, 2))
        eq(rotate(0, 0, 9), (9, 0, 0))
        eq(swapped(("a", "b")), ("b", "a"))
        eq(swapped(("only", "two")), ("two", "only"))
        """,
    ),
    dict(
        name="basics7",
        intro="""
        `==` asks "same value". `is` asks "same object in memory". They are
        not interchangeable.

        Use `is` only for None, True, False, and sentinel objects you created
        yourself. Using `is` on numbers or strings appears to work because
        CPython caches small integers and some strings -- and then fails on
        the one input that is not cached. That is a miserable bug to find.
        """,
        hint="""
        One function is `a == b`, the other is `a is b`. The names tell you
        which is which.
        """,
        stub="""
        def same_value(a: object, b: object) -> bool:
            return ...


        def same_object(a: object, b: object) -> bool:
            return ...
        """,
        solution="""
        def same_value(a: object, b: object) -> bool:
            return a == b


        def same_object(a: object, b: object) -> bool:
            return a is b
        """,
        checks="""
        xs = [1, 2]
        ys = [1, 2]

        ok(same_value(xs, ys), "two lists with equal contents are ==")
        not_ok(same_object(xs, ys), "but they are two different objects")
        ok(same_object(xs, xs))
        ok(same_value(None, None))
        ok(same_object(None, None), "None is a singleton -- there is only one")
        ok(same_value("ab", "a" + "b"))
        """,
    ),
]
