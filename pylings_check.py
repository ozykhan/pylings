"""Tiny assertion helpers so failures tell you what actually happened.

A bare `assert f(1) == 2` in plain Python just says "AssertionError" with no
values. These say what they expected and what they got.

You never need to edit this file.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, NoReturn


def _fail(label: str, detail: str) -> NoReturn:
    raise AssertionError(f"{label}\n{detail}")


def eq(actual: Any, expected: Any, label: str = "values differ") -> None:
    """Assert `actual == expected`."""
    if actual != expected:
        _fail(label, f"    expected: {expected!r}\n    actual:   {actual!r}")


def is_(actual: Any, expected: Any, label: str = "not the same object") -> None:
    """Assert `actual is expected` -- identity, not equality."""
    if actual is not expected:
        _fail(label, f"    expected: {expected!r} (id {id(expected)})\n"
                     f"    actual:   {actual!r} (id {id(actual)})")


def ok(value: Any, label: str = "expected a truthy value") -> None:
    if not value:
        _fail(label, f"    got: {value!r}")


def not_ok(value: Any, label: str = "expected a falsy value") -> None:
    if value:
        _fail(label, f"    got: {value!r}")


def raises(exc: type[BaseException], fn: Callable[[], Any], label: str = "") -> BaseException:
    """Assert that calling `fn` raises `exc`. Returns the exception."""
    label = label or f"expected {exc.__name__} to be raised"
    try:
        result = fn()
    except exc as caught:
        return caught
    except BaseException as caught:  # noqa: BLE001
        _fail(label, f"    raised {type(caught).__name__} instead: {caught}")
    _fail(label, f"    nothing was raised; returned {result!r}")
