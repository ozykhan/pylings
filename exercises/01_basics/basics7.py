# basics7.py
#
# `==` asks "same value". `is` asks "same object in memory". They are
# not interchangeable.
#
# Use `is` only for None, True, False, and sentinel objects you created
# yourself. Using `is` on numbers or strings appears to work because
# CPython caches small integers and some strings -- and then fails on
# the one input that is not cached. That is a miserable bug to find.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import ok, not_ok


def same_value(a: object, b: object) -> bool:
    return a == b


def same_object(a: object, b: object) -> bool:
    return a is b


# --- checks (do not edit) ------------------------------------------
xs = [1, 2]
ys = [1, 2]

ok(same_value(xs, ys), "two lists with equal contents are ==")
not_ok(same_object(xs, ys), "but they are two different objects")
ok(same_object(xs, xs))
ok(same_value(None, None))
ok(same_object(None, None), "None is a singleton -- there is only one")
ok(same_value("ab", "a" + "b"))
