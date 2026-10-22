# err6.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, raises

import contextlib
from collections.abc import Iterator


@contextlib.contextmanager
def tracked(log: list[str]) -> Iterator[str]:
    log.append("enter")
    try:
        yield "resource"
    finally:
        log.append("exit")


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
