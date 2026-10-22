# strings4.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def strip_protocol(url: str) -> str:
    return url.removeprefix("https://").removeprefix("http://")


# --- checks (do not edit) ------------------------------------------
eq(strip_protocol("https://example.com/a"), "example.com/a")
eq(strip_protocol("http://example.com"), "example.com")
eq(strip_protocol("ftp://example.com"), "ftp://example.com")
eq(strip_protocol("example.com"), "example.com")
eq(strip_protocol(""), "")
