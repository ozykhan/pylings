# basics2.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, ok, not_ok

def is_blank(value: object) -> bool:
    return not value


# --- checks (do not edit) ------------------------------------------
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
