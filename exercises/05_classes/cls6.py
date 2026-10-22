# cls6.py
#
# @dataclass writes __init__, __repr__ and __eq__ for you from the
# annotated fields. It is the default choice for anything that mostly
# holds data.
#
#   frozen=True   immutable -- assignment raises, and you get __hash__
#   slots=True    no per-instance __dict__: less memory, faster
#                 attribute access, and typos raise instead of quietly
#                 creating a new attribute
#
# Fields with defaults must come after fields without.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, ok, not_ok, raises

from dataclasses import dataclass


# TODO: make this a frozen, slotted dataclass with fields
#       host: str  and  port: int = 8080
class Config:
    ...


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
