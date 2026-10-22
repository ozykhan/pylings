SECTION = "04_functions"

EXERCISES = [
    dict(
        name="func1",
        intro="""
        Parameters can have defaults, and callers can pass arguments by name
        in any order:

            def f(a, b=2, c=3): ...
            f(1, c=9)

        Named arguments at the call site are ordinary Python, not a special
        options-object pattern. Use them freely -- f(timeout=5) reads better
        than f(5).
        """,
        hint="""
        Give path a default of "/" and scheme a default of "https" in the
        signature, then build the URL with an f-string.
        """,
        stub="""
        def make_url(host: str, path, scheme) -> str:
            # TODO: give path the default "/" and scheme the default "https"
            return ...
        """,
        solution="""
        def make_url(host: str, path: str = "/", scheme: str = "https") -> str:
            return f"{scheme}://{host}{path}"
        """,
        checks="""
        eq(make_url("example.com"), "https://example.com/")
        eq(make_url("example.com", "/docs"), "https://example.com/docs")
        eq(make_url("example.com", scheme="http"), "http://example.com/")
        eq(make_url("example.com", "/a", "http"), "http://example.com/a")
        eq(make_url(path="/x", host="example.com"), "https://example.com/x")
        """,
    ),
    dict(
        name="func2",
        intro="""
        THE Python gotcha. A default argument is evaluated ONCE, when the
        function is defined -- not on each call. So this is broken:

            def add(item, basket=[]):   # the SAME list every call
                basket.append(item)
                return basket

        Call it twice and the second call still has the first item in it.
        The fix is always the same: default to None and build the real value
        inside the body.
        """,
        hint="""
        Signature: basket: list[str] | None = None
        Body: if basket is None, assign a fresh [] to it, then append and
        return.
        """,
        stub="""
        def add_item(item: str, basket: list[str] | None = None) -> list[str]:
            # Append item to basket and return it.
            # When no basket is given, start a FRESH empty one each call.
            ...
        """,
        solution="""
        def add_item(item: str, basket: list[str] | None = None) -> list[str]:
            if basket is None:
                basket = []
            basket.append(item)
            return basket
        """,
        checks="""
        eq(add_item("a"), ["a"])
        eq(add_item("b"), ["b"], "a fresh list each call -- not ['a', 'b']")
        eq(add_item("c"), ["c"])

        mine = ["x"]
        eq(add_item("y", mine), ["x", "y"])
        eq(mine, ["x", "y"], "a basket that was passed in is appended to in place")

        # Demonstration of the bug, so you have seen it happen.
        def broken(item, basket=[]):
            basket.append(item)
            return basket

        eq(broken(1), [1])
        eq(broken(2), [1, 2], "the default list survived between calls")
        """,
    ),
    dict(
        name="func3",
        intro="""
        *args collects extra positional arguments into a tuple.
        **kwargs collects extra named arguments into a dict.

        The names are convention, the stars are the syntax. At a call site
        the same stars do the reverse: f(*items) spreads a list into
        positional arguments, f(**options) spreads a dict into named ones.
        """,
        hint="""
        tally: sum(numbers) plus start.
        to_query: join over params.items() with an f-string for each pair.
        """,
        stub="""
        def tally(*numbers: int, start: int = 0) -> int:
            # Add up every positional argument, beginning from start.
            return ...


        def to_query(**params: str) -> str:
            # "a=1&b=2", in the order the arguments were given.
            return ...
        """,
        solution="""
        def tally(*numbers: int, start: int = 0) -> int:
            return start + sum(numbers)


        def to_query(**params: str) -> str:
            return "&".join(f"{key}={value}" for key, value in params.items())
        """,
        checks="""
        eq(tally(), 0)
        eq(tally(1, 2, 3), 6)
        eq(tally(1, 2, start=10), 13)
        eq(tally(*[1, 2, 3]), 6, "a star at the call site spreads the list")

        eq(to_query(), "")
        eq(to_query(a="1"), "a=1")
        eq(to_query(a="1", b="2"), "a=1&b=2")
        eq(to_query(**{"q": "python", "page": "2"}), "q=python&page=2")
        """,
    ),
    dict(
        name="func4",
        intro="""
        A bare * in a signature means "everything after me must be passed by
        name":

            def connect(host, *, port, timeout=5.0): ...
            connect("db", port=5432)        # fine
            connect("db", 5432)             # TypeError

        Do this for any parameter whose meaning is not obvious at the call
        site. connect("db", 5432, 5.0) is unreadable; forcing names fixes it
        permanently, and you can reorder the parameters later without
        breaking callers.
        """,
        hint="""
        Put a bare * after host. port has no default, timeout defaults to
        5.0. The body is one f-string.
        """,
        stub="""
        def connect(host: str, port: int, timeout: float = 5.0) -> str:
            # TODO: make port and timeout keyword-only.
            return ...
        """,
        solution="""
        def connect(host: str, *, port: int, timeout: float = 5.0) -> str:
            return f"{host}:{port} t={timeout}"
        """,
        checks="""
        eq(connect("db", port=5432), "db:5432 t=5.0")
        eq(connect("db", port=5432, timeout=1.5), "db:5432 t=1.5")
        raises(TypeError, lambda: connect("db", 5432), "port must be keyword-only")
        """,
    ),
    dict(
        name="func5",
        intro="""
        Functions are objects. You can define one inside another, return it,
        and it keeps a reference to the enclosing scope. That is a closure --
        exactly as in JavaScript.

        One difference: assigning to a name inside a function makes it local
        by default. To assign to a name from the enclosing function you must
        say `nonlocal` first. (`global` is the module-level equivalent, and
        you should almost never need it.)
        """,
        hint="""
        make_multiplier: define an inner function that returns n * factor,
        then return the inner function itself -- no parentheses.
        make_counter: the inner function needs `nonlocal count` before it can
        do count += 1.
        """,
        stub="""
        from collections.abc import Callable


        def make_multiplier(factor: int) -> Callable[[int], int]:
            # Return a function that multiplies its argument by factor.
            ...


        def make_counter() -> Callable[[], int]:
            # Return a function that returns 1, then 2, then 3, ...
            # Each counter made here is independent.
            ...
        """,
        solution="""
        from collections.abc import Callable


        def make_multiplier(factor: int) -> Callable[[int], int]:
            def multiply(n: int) -> int:
                return n * factor

            return multiply


        def make_counter() -> Callable[[], int]:
            count = 0

            def tick() -> int:
                nonlocal count
                count += 1
                return count

            return tick
        """,
        checks="""
        double = make_multiplier(2)
        triple = make_multiplier(3)
        eq(double(5), 10)
        eq(triple(5), 15)
        eq(double(5), 10, "the closure keeps working")

        counter = make_counter()
        eq(counter(), 1)
        eq(counter(), 2)
        eq(counter(), 3)
        eq(make_counter()(), 1, "a second counter starts from scratch")
        """,
    ),
    dict(
        name="func6",
        intro="""
        A decorator is a function that takes a function and returns a
        replacement. The @ syntax is only shorthand:

            @logged
            def work(): ...

            # is exactly
            work = logged(work)

        Always wrap the replacement with functools.wraps, or the decorated
        function loses its own __name__ and docstring -- which breaks
        tracebacks, debuggers and anything that introspects.
        """,
        hint="""
        Inside `logged`, define wrapper(*args, **kwargs), record fn.__name__
        in CALLS, then return fn(*args, **kwargs). Put @functools.wraps(fn)
        on wrapper, and return wrapper from logged.
        """,
        stub="""
        import functools
        from collections.abc import Callable
        from typing import Any

        CALLS: list[str] = []


        def logged(fn: Callable[..., Any]) -> Callable[..., Any]:
            # Return a replacement that appends fn.__name__ to CALLS, then
            # calls fn with whatever arguments it was given and returns the
            # result unchanged.
            ...
        """,
        solution="""
        import functools
        from collections.abc import Callable
        from typing import Any

        CALLS: list[str] = []


        def logged(fn: Callable[..., Any]) -> Callable[..., Any]:
            @functools.wraps(fn)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                CALLS.append(fn.__name__)
                return fn(*args, **kwargs)

            return wrapper
        """,
        checks="""
        @logged
        def add(a: int, b: int = 0) -> int:
            "Adds two numbers."
            return a + b


        eq(add(1, 2), 3, "the wrapper must return the real result")
        eq(add(1, b=5), 6, "keyword arguments must pass through")
        eq(CALLS, ["add", "add"])
        eq(add.__name__, "add", "use functools.wraps to keep the name")
        eq(add.__doc__, "Adds two numbers.", "and the docstring")
        """,
    ),
    dict(
        name="func7",
        intro="""
        functools.cache memoizes a function: same arguments, same answer,
        computed once. It is one line and it is in the standard library.

        The arguments must be hashable, so this works for ints and strings
        and tuples, and not for lists or dicts. There is also
        functools.lru_cache(maxsize=N) when you need a bound on memory.
        """,
        hint="""
        Put @functools.cache directly above the def. That is the entire
        change.
        """,
        stub="""
        import functools

        COMPUTED: list[int] = []


        def slow_square(n: int) -> int:
            # TODO: memoize this so repeated arguments are computed once.
            COMPUTED.append(n)
            return n * n
        """,
        solution="""
        import functools

        COMPUTED: list[int] = []


        @functools.cache
        def slow_square(n: int) -> int:
            COMPUTED.append(n)
            return n * n
        """,
        checks="""
        eq(slow_square(3), 9)
        eq(slow_square(3), 9)
        eq(slow_square(3), 9)
        eq(COMPUTED, [3], "computed once, then served from the cache")

        eq(slow_square(4), 16)
        eq(COMPUTED, [3, 4], "a new argument really is computed")

        raises(TypeError, lambda: slow_square([1]), "cache keys must be hashable")
        """,
    ),
]
