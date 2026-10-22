# err5.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, is_, raises

class Tracker:
    def __init__(self) -> None:
        self.events: list[str] = []

    def __enter__(self) -> "Tracker":
        self.events.append("enter")
        return self

    def __exit__(self, exc_type: object, exc: object, tb: object) -> bool:
        self.events.append("exit")
        return False


# --- checks (do not edit) ------------------------------------------
tracker = Tracker()
with tracker as handle:
    is_(handle, tracker, "__enter__ should return the tracker itself")
    handle.events.append("body")
eq(tracker.events, ["enter", "body", "exit"])


def boom() -> None:
    with Tracker() as t:
        FAILED.append(t)
        raise RuntimeError("boom")


FAILED: list[Tracker] = []
raises(RuntimeError, boom, "the exception must not be swallowed")
eq(FAILED[0].events, ["enter", "exit"], "but __exit__ still ran")
