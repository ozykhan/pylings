# err6.py
#
# Writing __enter__/__exit__ by hand is rarely worth it.
# @contextlib.contextmanager turns a generator into a context manager:
# everything before the yield is setup, the yielded value is what `as`
# binds, and everything after is teardown.
#
# Put the teardown in a finally block, or it will not run when the
# body raises -- which is the entire reason you wanted a context
# manager.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, raises

import contextlib
from collections.abc import Iterator


# TODO: make this a context manager.
def tracked(log: list[str]) -> Iterator[str]:
    # Append "enter", hand out the string "resource", and append
    # "exit" afterwards -- even if the body raised.
    ...


# --- checks (do not edit) ------------------------------------------
log: list[str] = []
with tracked(log) as resource:
    eq(resource, "resource")
    log.append("body")
eq(log, ["enter", "body", "exit"])


def boom() -> None:
    with tracked(failing):
        raise RuntimeError("boom")


failing: list[str] = []
raises(RuntimeError, boom)
eq(failing, ["enter", "exit"], "teardown must run on failure -- use try/finally")
