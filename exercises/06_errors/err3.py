# err3.py
#
# Define your own exceptions, and inherit from the closest built-in
# that fits -- ValueError for bad values, KeyError for missing keys,
# and so on. A caller doing broad validation can then catch ValueError
# and still catch yours.
#
# Store the structured details as attributes. A message string that
# something has to parse later is not an API.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, ok, raises

class ValidationError(...):
    # TODO: inherit from ValueError.
    # __init__(self, field, reason) stores both as attributes and
    # passes f"{field}: {reason}" up to the base class.
    ...


def validate_age(age: int) -> int:
    # Raise ValidationError("age", "must not be negative") when
    # age is below zero. Otherwise return it.
    ...


# --- checks (do not edit) ------------------------------------------
eq(validate_age(0), 0)
eq(validate_age(41), 41)

err = raises(ValidationError, lambda: validate_age(-1))
eq(err.field, "age")
eq(err.reason, "must not be negative")
eq(str(err), "age: must not be negative")
ok(isinstance(err, ValueError), "inherit from the closest built-in")

# So a caller who only knows about ValueError still catches it.
raises(ValueError, lambda: validate_age(-5))
