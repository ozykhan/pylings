# cls5.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, ok, not_ok

class Duration:
    def __init__(self, seconds: int) -> None:
        self.seconds = seconds

    @classmethod
    def from_minutes(cls, minutes: int) -> "Duration":
        return cls(minutes * 60)

    @staticmethod
    def is_valid(seconds: int) -> bool:
        return seconds >= 0


# --- checks (do not edit) ------------------------------------------
eq(Duration.from_minutes(3).seconds, 180)
eq(Duration.from_minutes(0).seconds, 0)
ok(Duration.is_valid(0))
not_ok(Duration.is_valid(-1))
ok(Duration.is_valid(5))

# Because from_minutes builds with cls(...), subclasses get their own type.
class Timeout(Duration):
    pass

eq(type(Timeout.from_minutes(1)), Timeout)
