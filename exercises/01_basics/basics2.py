# basics2.py
#
# Every Python object is either truthy or falsy. The falsy ones are:
# False, None, 0, 0.0, "" and every empty container -- [], {}, set(),
# (). Everything else is truthy.
#
# This is why `if items:` is the idiomatic way to ask "is this list
# non-empty", rather than `if len(items) > 0`.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, ok, not_ok


def is_blank(value: object) -> bool:
    if value:
        return False

    return True


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
