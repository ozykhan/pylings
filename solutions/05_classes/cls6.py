# cls6.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, ok, not_ok, raises

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Config:
    host: str
    port: int = 8080


# --- checks (do not edit) ------------------------------------------
c = Config("db.example.com")
eq(c.host, "db.example.com")
eq(c.port, 8080)
eq(Config("a", 1), Config("a", 1), "__eq__ compares field by field")
not_ok(Config("a", 1) == Config("a", 2))
eq(repr(Config("a", 1)), "Config(host='a', port=1)")
ok(hash(Config("a", 1)) == hash(Config("a", 1)), "frozen dataclasses hash")
raises(Exception, lambda: setattr(c, "host", "other"), "frozen means frozen")
not_ok(hasattr(c, "__dict__"), "slots=True removes the per-instance dict")
