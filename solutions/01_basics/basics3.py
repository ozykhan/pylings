# basics3.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def resolve_port(port: int | None) -> int:
    return 8080 if port is None else port


# --- checks (do not edit) ------------------------------------------
eq(resolve_port(None), 8080, "no port given -> the default")
eq(resolve_port(0), 0, "0 was given explicitly -- do not replace it")
eq(resolve_port(3000), 3000)
