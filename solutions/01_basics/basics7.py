# basics7.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

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
