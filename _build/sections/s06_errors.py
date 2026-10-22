SECTION = "06_errors"

EXERCISES = [
    dict(
        name="err1",
        intro="""
        Python leans on exceptions far more than JavaScript does. Iteration,
        attribute lookup and dict access are all built on them, and "try it
        and handle the failure" is idiomatic rather than sloppy.

        Catch the specific exception you expect. A bare `except:` also
        catches KeyboardInterrupt and SystemExit, which is how a program
        becomes impossible to stop.
        """,
        hint="""
        try: return int(text)
        except ValueError: return default
        """,
        stub="""
        def safe_int(text: str, default: int = 0) -> int:
            # Parse text as an int. If it is not a number, return default.
            ...
        """,
        solution="""
        def safe_int(text: str, default: int = 0) -> int:
            try:
                return int(text)
            except ValueError:
                return default
        """,
        checks="""
        eq(safe_int("12"), 12)
        eq(safe_int("-3"), -3)
        eq(safe_int("  7 "), 7, "int() ignores surrounding whitespace")
        eq(safe_int("abc"), 0)
        eq(safe_int(""), 0)
        eq(safe_int("1.5"), 0, "int() will not parse a decimal point")
        eq(safe_int("abc", -1), -1)
        """,
    ),
    dict(
        name="err2",
        intro="""
        try has four parts, and the two people forget are the useful ones:

          try     the code that might fail
          except  runs only if it did
          else    runs only if it did NOT -- keeps the try block down to the
                  one line that can actually raise
          finally always runs, even on return or on an exception you are not
                  catching. This is where cleanup goes.
        """,
        hint="""
        Put the division in try. In except ZeroDivisionError, append "error"
        and return None. In else, append "ok" and return the result. In
        finally, append "cleanup".
        """,
        stub="""
        EVENTS: list[str] = []


        def divide(a: float, b: float) -> float | None:
            # Append "ok" on success, "error" on division by zero, and
            # "cleanup" either way -- in that order.
            # Return the result, or None when it failed.
            EVENTS.clear()
            ...
        """,
        solution="""
        EVENTS: list[str] = []


        def divide(a: float, b: float) -> float | None:
            EVENTS.clear()
            try:
                result = a / b
            except ZeroDivisionError:
                EVENTS.append("error")
                return None
            else:
                EVENTS.append("ok")
                return result
            finally:
                EVENTS.append("cleanup")
        """,
        checks="""
        eq(divide(6, 3), 2.0)
        eq(EVENTS, ["ok", "cleanup"])

        eq(divide(1, 0), None)
        eq(EVENTS, ["error", "cleanup"], "finally runs even after a return")
        """,
    ),
    dict(
        name="err3",
        intro="""
        Define your own exceptions, and inherit from the closest built-in
        that fits -- ValueError for bad values, KeyError for missing keys,
        and so on. A caller doing broad validation can then catch ValueError
        and still catch yours.

        Store the structured details as attributes. A message string that
        something has to parse later is not an API.
        """,
        hint="""
        class ValidationError(ValueError). In __init__, store field and
        reason on self, then call super().__init__ with the combined
        message so str(exc) works.
        """,
        stub="""
        class ValidationError(...):
            # TODO: inherit from ValueError.
            # __init__(self, field, reason) stores both as attributes and
            # passes f"{field}: {reason}" up to the base class.
            ...


        def validate_age(age: int) -> int:
            # Raise ValidationError("age", "must not be negative") when
            # age is below zero. Otherwise return it.
            ...
        """,
        solution="""
        class ValidationError(ValueError):
            def __init__(self, field: str, reason: str) -> None:
                self.field = field
                self.reason = reason
                super().__init__(f"{field}: {reason}")


        def validate_age(age: int) -> int:
            if age < 0:
                raise ValidationError("age", "must not be negative")
            return age
        """,
        checks="""
        eq(validate_age(0), 0)
        eq(validate_age(41), 41)

        err = raises(ValidationError, lambda: validate_age(-1))
        eq(err.field, "age")
        eq(err.reason, "must not be negative")
        eq(str(err), "age: must not be negative")
        ok(isinstance(err, ValueError), "inherit from the closest built-in")

        # So a caller who only knows about ValueError still catches it.
        raises(ValueError, lambda: validate_age(-5))
        """,
    ),
    dict(
        name="err4",
        intro="""
        When you catch a low-level failure and re-raise something meaningful,
        keep the original attached:

            raise ConfigError(...) from exc

        The traceback then shows both, joined by "The above exception was the
        direct cause of the following exception". Without `from`, Python
        still shows the original but describes it as an accident
        ("During handling of the above exception, another occurred").

        `raise X from None` deliberately hides the original. Use it rarely.
        """,
        hint="""
        try: return int(raw)
        except ValueError as exc:
            raise ConfigError(f"bad port: {raw!r}") from exc
        """,
        stub="""
        class ConfigError(Exception):
            pass


        def load_port(raw: str) -> int:
            # Parse raw as an int. On failure raise
            # ConfigError(f"bad port: {raw!r}") with the original ValueError
            # attached as its cause.
            ...
        """,
        solution="""
        class ConfigError(Exception):
            pass


        def load_port(raw: str) -> int:
            try:
                return int(raw)
            except ValueError as exc:
                raise ConfigError(f"bad port: {raw!r}") from exc
        """,
        checks="""
        eq(load_port("8080"), 8080)

        err = raises(ConfigError, lambda: load_port("http"))
        eq(str(err), "bad port: 'http'")
        ok(isinstance(err.__cause__, ValueError), "use `from exc` to set __cause__")
        """,
    ),
    dict(
        name="err5",
        intro="""
        The `with` statement guarantees cleanup. Any object with __enter__
        and __exit__ can be used with it.

        __enter__ returns whatever the `as` name binds to.
        __exit__ is called no matter how the block ends. Return False (or
        None) from it to let an exception continue; returning True swallows
        the exception, which you should do only when you really mean it.
        """,
        hint="""
        __enter__ appends "enter" to self.events and returns self.
        __exit__ takes (self, exc_type, exc, tb), appends "exit", and
        returns False.
        """,
        stub="""
        class Tracker:
            def __init__(self) -> None:
                self.events: list[str] = []

            # TODO: __enter__ -- record "enter", hand back the tracker itself

            # TODO: __exit__ -- record "exit", do not swallow exceptions
        """,
        solution="""
        class Tracker:
            def __init__(self) -> None:
                self.events: list[str] = []

            def __enter__(self) -> "Tracker":
                self.events.append("enter")
                return self

            def __exit__(self, exc_type: object, exc: object, tb: object) -> bool:
                self.events.append("exit")
                return False
        """,
        checks="""
        tracker = Tracker()
        with tracker as handle:
            is_(handle, tracker, "__enter__ should return the tracker itself")
            handle.events.append("body")
        eq(tracker.events, ["enter", "body", "exit"])


        def boom() -> None:
            with Tracker() as t:
                FAILED.append(t)
                raise RuntimeError("boom")


        FAILED: list[Tracker] = []
        raises(RuntimeError, boom, "the exception must not be swallowed")
        eq(FAILED[0].events, ["enter", "exit"], "but __exit__ still ran")
        """,
    ),
    dict(
        name="err6",
        intro="""
        Writing __enter__/__exit__ by hand is rarely worth it.
        @contextlib.contextmanager turns a generator into a context manager:
        everything before the yield is setup, the yielded value is what `as`
        binds, and everything after is teardown.

        Put the teardown in a finally block, or it will not run when the
        body raises -- which is the entire reason you wanted a context
        manager.
        """,
        hint="""
        Decorate with @contextlib.contextmanager. Append "enter" to log,
        then `try: yield "resource"` and `finally: log.append("exit")`.
        """,
        stub="""
        import contextlib
        from collections.abc import Iterator


        # TODO: make this a context manager.
        def tracked(log: list[str]) -> Iterator[str]:
            # Append "enter", hand out the string "resource", and append
            # "exit" afterwards -- even if the body raised.
            ...
        """,
        solution="""
        import contextlib
        from collections.abc import Iterator


        @contextlib.contextmanager
        def tracked(log: list[str]) -> Iterator[str]:
            log.append("enter")
            try:
                yield "resource"
            finally:
                log.append("exit")
        """,
        checks="""
        log: list[str] = []
        with tracked(log) as resource:
            eq(resource, "resource")
            log.append("body")
        eq(log, ["enter", "body", "exit"])


        def boom() -> None:
            with tracked(failing):
                raise RuntimeError("boom")


        failing: list[str] = []
        raises(RuntimeError, boom)
        eq(failing, ["enter", "exit"], "teardown must run on failure -- use try/finally")
        """,
    ),
]
