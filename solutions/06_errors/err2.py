# err2.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

EVENTS: list[str] = []


def divide(a: float, b: float) -> float | None:
    EVENTS.clear()
    try:
        result = a / b
    except ZeroDivisionError:
        EVENTS.append("error")
        return None
    else:
        EVENTS.append("ok")
        return result
    finally:
        EVENTS.append("cleanup")


# --- checks (do not edit) ------------------------------------------
eq(divide(6, 3), 2.0)
eq(EVENTS, ["ok", "cleanup"])

eq(divide(1, 0), None)
eq(EVENTS, ["error", "cleanup"], "finally runs even after a return")
