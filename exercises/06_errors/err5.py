# err5.py
#
# The `with` statement guarantees cleanup. Any object with __enter__
# and __exit__ can be used with it.
#
# __enter__ returns whatever the `as` name binds to.
# __exit__ is called no matter how the block ends. Return False (or
# None) from it to let an exception continue; returning True swallows
# the exception, which you should do only when you really mean it.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, is_, raises

class Tracker:
    def __init__(self) -> None:
        self.events: list[str] = []

    # TODO: __enter__ -- record "enter", hand back the tracker itself

    # TODO: __exit__ -- record "exit", do not swallow exceptions


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
