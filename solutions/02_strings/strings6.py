# strings6.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def byte_length(text: str) -> int:
    return len(text.encode("utf-8"))


# --- checks (do not edit) ------------------------------------------
eq(byte_length("abc"), 3)
eq(byte_length(""), 0)
eq(byte_length("ğ"), 2, "one character, two bytes")
eq(byte_length("İstanbul"), 9, "eight characters, nine bytes")

# Demonstration: the two lengths genuinely differ.
eq(len("İstanbul"), 8)
eq(type("a".encode()).__name__, "bytes")
eq(b"abc".decode("utf-8"), "abc")
