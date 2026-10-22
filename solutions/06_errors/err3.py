# err3.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, ok, raises

class ValidationError(ValueError):
    def __init__(self, field: str, reason: str) -> None:
        self.field = field
        self.reason = reason
        super().__init__(f"{field}: {reason}")


def validate_age(age: int) -> int:
    if age < 0:
        raise ValidationError("age", "must not be negative")
    return age


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
