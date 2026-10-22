# cls5.py
#
# Two more decorators for methods:
#
#   @classmethod   receives the class as `cls`. The standard way to
#                  write alternative constructors, and using cls(...)
#                  rather than the class name means subclasses get the
#                  right type back.
#   @staticmethod  receives nothing special. A plain function that
#                  lives in the class's namespace because it belongs
#                  there conceptually.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, ok, not_ok

class Duration:
    def __init__(self, seconds: int) -> None:
        self.seconds = seconds

    # TODO: an alternative constructor Duration.from_minutes(3)

    # TODO: a validator Duration.is_valid(-1) -> False


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
