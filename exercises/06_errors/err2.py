# err2.py
#
# try has four parts, and the two people forget are the useful ones:
#
#   try     the code that might fail
#   except  runs only if it did
#   else    runs only if it did NOT -- keeps the try block down to the
#           one line that can actually raise
#   finally always runs, even on return or on an exception you are not
#           catching. This is where cleanup goes.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

EVENTS: list[str] = []


def divide(a: float, b: float) -> float | None:
    # Append "ok" on success, "error" on division by zero, and
    # "cleanup" either way -- in that order.
    # Return the result, or None when it failed.
    EVENTS.clear()
    ...


# --- checks (do not edit) ------------------------------------------
eq(divide(6, 3), 2.0)
eq(EVENTS, ["ok", "cleanup"])

eq(divide(1, 0), None)
eq(EVENTS, ["error", "cleanup"], "finally runs even after a return")
