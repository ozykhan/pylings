# func4.py
#
# A bare * in a signature means "everything after me must be passed by
# name":
#
#     def connect(host, *, port, timeout=5.0): ...
#     connect("db", port=5432)        # fine
#     connect("db", 5432)             # TypeError
#
# Do this for any parameter whose meaning is not obvious at the call
# site. connect("db", 5432, 5.0) is unreadable; forcing names fixes it
# permanently, and you can reorder the parameters later without
# breaking callers.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, raises

def connect(host: str, port: int, timeout: float = 5.0) -> str:
    # TODO: make port and timeout keyword-only.
    return ...


# --- checks (do not edit) ------------------------------------------
eq(connect("db", port=5432), "db:5432 t=5.0")
eq(connect("db", port=5432, timeout=1.5), "db:5432 t=1.5")
raises(TypeError, lambda: connect("db", 5432), "port must be keyword-only")
