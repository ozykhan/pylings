SECTION = "08_typing"

EXERCISES = [
    dict(
        name="typ1",
        intro="""
        Type hints are optional and Python does not enforce them at runtime.
        A checker like mypy reads them -- that is the whole point, the same
        split you have between tsc and the JavaScript that actually runs.

        Syntax: `name: type` for parameters, `-> type` for the return.

        These exercises verify your annotations with typing.get_type_hints,
        which reads them back at runtime, so you can see that they are real
        objects and not comments.
        """,
        hint="""
        text is a str, times is an int, and the function returns a str:
            def repeat(text: str, times: int) -> str:
        """,
        stub="""
        def repeat(text, times):
            # TODO: annotate the parameters and the return type.
            return text * times
        """,
        solution="""
        def repeat(text: str, times: int) -> str:
            return text * times
        """,
        checks="""
        from typing import get_type_hints

        eq(repeat("ab", 2), "abab")
        eq(
            get_type_hints(repeat),
            {"text": str, "times": int, "return": str},
            "annotate both parameters and the return",
        )

        # Demonstration: nothing is enforced at runtime. Annotations describe
        # intent to a checker; they do not validate.
        eq(repeat([0], 2), [0, 0], "a list still works -- mypy is what would complain")
        """,
    ),
    dict(
        name="typ2",
        intro="""
        A value that may be missing is written `int | None`. The older
        spelling is Optional[int]; they mean the same thing and the | form
        is preferred now.

        Optional does NOT mean "this argument can be left out" -- it means
        "None is one of the allowed values". A parameter is made optional by
        giving it a default, which is a separate thing.
        """,
        hint="""
        .get returns None when the key is missing, so the return type is
        int | None.
        """,
        stub="""
        def find_score(scores: dict[str, int], name: str):
            # TODO: annotate the return type. It can return None.
            return scores.get(name)
        """,
        solution="""
        def find_score(scores: dict[str, int], name: str) -> int | None:
            return scores.get(name)
        """,
        checks="""
        from typing import get_type_hints

        eq(find_score({"a": 1}, "a"), 1)
        eq(find_score({"a": 1}, "b"), None)
        eq(
            get_type_hints(find_score)["return"],
            int | None,
            "the return type should be int | None",
        )
        """,
    ),
    dict(
        name="typ3",
        intro="""
        Containers are annotated with what they hold: list[str],
        dict[str, int], tuple[int, int], set[str].

        Since Python 3.9 you use the built-in names directly. If you see
        `from typing import List, Dict` in a tutorial, it is old -- those
        are deprecated aliases.

        For a parameter, prefer the most general type you actually need:
        Sequence[str] or Iterable[str] rather than list[str], so a caller
        can pass a tuple or a generator.
        """,
        hint="""
        words is a list of strings, and the result maps each string to its
        integer length:
            def length_index(words: list[str]) -> dict[str, int]:
        """,
        stub="""
        def length_index(words):
            # TODO: annotate. It takes a list of strings and returns a dict
            # mapping each string to its length.
            return {word: len(word) for word in words}
        """,
        solution="""
        def length_index(words: list[str]) -> dict[str, int]:
            return {word: len(word) for word in words}
        """,
        checks="""
        from typing import get_type_hints

        eq(length_index(["a", "bbb"]), {"a": 1, "bbb": 3})
        eq(
            get_type_hints(length_index),
            {"words": list[str], "return": dict[str, int]},
            "use the built-in generics, not typing.List / typing.Dict",
        )
        """,
    ),
    dict(
        name="typ4",
        intro="""
        A TypeVar links types together. `def first(items: Sequence[T],
        default: T) -> T` says: whatever the sequence holds, the default and
        the result are that same type. Annotating it as `object` would lose
        exactly that.

        Python 3.12 added a shorter spelling -- `def first[T](...)` -- with
        no TypeVar declaration. The explicit form here still works
        everywhere and is what you will meet in existing code.
        """,
        hint="""
        Loop over items and return the first one you see; if the loop ends
        without returning, return default.
        """,
        stub="""
        from collections.abc import Sequence
        from typing import TypeVar

        T = TypeVar("T")


        def first(items: Sequence[T], default: T) -> T:
            # The first item, or default when there are none.
            ...
        """,
        solution="""
        from collections.abc import Sequence
        from typing import TypeVar

        T = TypeVar("T")


        def first(items: Sequence[T], default: T) -> T:
            for item in items:
                return item
            return default
        """,
        checks="""
        eq(first([1, 2], 0), 1)
        eq(first([], 99), 99)
        eq(first("abc", "z"), "a", "a str is a Sequence too")
        eq(first((), "fallback"), "fallback")
        eq(first([None, 1], "x"), None, "the first item may itself be falsy")
        """,
    ),
    dict(
        name="typ5",
        intro="""
        A Protocol describes a shape. Any class with matching members
        satisfies it -- no inheritance, no registration. This is the
        structural typing you are used to from TypeScript interfaces, and it
        is the right tool for "anything with a .close() method".

        Add @runtime_checkable and isinstance() starts working too, though
        it only checks that the method names exist, not their signatures.
        """,
        hint="""
        Decorate with @runtime_checkable, inherit from Protocol, and declare
        the method with an ellipsis body:

            @runtime_checkable
            class Closeable(Protocol):
                def close(self) -> None: ...
        """,
        stub="""
        from typing import Protocol, runtime_checkable


        # TODO: a runtime-checkable Protocol named Closeable describing
        #       anything with a close() method taking no arguments.
        class Closeable:
            ...
        """,
        solution="""
        from typing import Protocol, runtime_checkable


        @runtime_checkable
        class Closeable(Protocol):
            def close(self) -> None: ...
        """,
        checks="""
        class Socket:
            def close(self) -> None:
                pass


        class Rock:
            pass


        ok(isinstance(Socket(), Closeable), "Socket has close(), so it fits the shape")
        not_ok(isinstance(Rock(), Closeable))
        not_ok(issubclass(Socket, Rock), "and it inherits from nothing")
        ok(issubclass(Socket, Closeable), "structural, not nominal")
        """,
    ),
    dict(
        name="typ6",
        intro="""
        A TypedDict describes the shape of a dict whose keys are known --
        JSON payloads, rows from a database driver, config blobs. At runtime
        it is an ordinary dict with no overhead; the structure exists only
        for the checker.

        NotRequired[...] marks a key that may be absent. Reach for a
        dataclass when you control the data, and a TypedDict when you are
        describing a dict someone else's code hands you.
        """,
        hint="""
        Inherit from TypedDict and declare the three keys as annotations.
        Wrap only the email one in NotRequired:

            class UserRow(TypedDict):
                id: int
                name: str
                email: NotRequired[str]
        """,
        stub="""
        from typing import NotRequired, TypedDict


        # TODO: a TypedDict named UserRow with
        #       id: int, name: str, and an optional email: str
        class UserRow:
            ...
        """,
        solution="""
        from typing import NotRequired, TypedDict


        class UserRow(TypedDict):
            id: int
            name: str
            email: NotRequired[str]
        """,
        checks="""
        eq(UserRow.__required_keys__, frozenset({"id", "name"}))
        eq(UserRow.__optional_keys__, frozenset({"email"}), "wrap email in NotRequired")
        eq(UserRow.__annotations__["id"], int)
        eq(UserRow.__annotations__["name"], str)

        # At runtime it is just a dict -- no validation, no class instance.
        row: UserRow = {"id": 1, "name": "faruk"}
        eq(row["name"], "faruk")
        eq(type(row), dict)
        """,
    ),
]
