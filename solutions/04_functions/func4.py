# func4.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, raises

def connect(host: str, *, port: int, timeout: float = 5.0) -> str:
    return f"{host}:{port} t={timeout}"


# --- checks (do not edit) ------------------------------------------
eq(connect("db", port=5432), "db:5432 t=5.0")
eq(connect("db", port=5432, timeout=1.5), "db:5432 t=1.5")
raises(TypeError, lambda: connect("db", 5432), "port must be keyword-only")
