# strings6.py
#
# A `str` is a sequence of characters. A `bytes` is a sequence of bytes.
# They are different types and Python will not quietly convert between
# them -- you encode a str to bytes and decode bytes back to a str.
#
# This matters the moment you touch a network, a file, or a Content-Length
# header, because len() of the two is not the same number.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def byte_length(text: str) -> int:
    # How many BYTES this text takes in UTF-8 -- not how many characters.
    return len(text.encode(encoding="utf-8"))


# --- checks (do not edit) ------------------------------------------
eq(byte_length("abc"), 3)
eq(byte_length(""), 0)
eq(byte_length("ğ"), 2, "one character, two bytes")
eq(byte_length("İstanbul"), 9, "eight characters, nine bytes")

# Demonstration: the two lengths genuinely differ.
eq(len("İstanbul"), 8)
eq(type("a".encode()).__name__, "bytes")
eq(b"abc".decode("utf-8"), "abc")
