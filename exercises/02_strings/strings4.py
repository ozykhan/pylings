# strings4.py
#
# removeprefix / removesuffix strip an affix only if it is actually
# there, and leave the string alone otherwise. Before they existed
# people wrote `if s.startswith(p): s = s[len(p):]` and got the length
# wrong.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def strip_protocol(url: str) -> str:
    # Remove a leading http:// or https://.
    # Anything else is returned unchanged.

    return url.removeprefix("http://").removeprefix("https://")


# --- checks (do not edit) ------------------------------------------
eq(strip_protocol("https://example.com/a"), "example.com/a")
eq(strip_protocol("http://example.com"), "example.com")
eq(strip_protocol("ftp://example.com"), "ftp://example.com")
eq(strip_protocol("example.com"), "example.com")
eq(strip_protocol(""), "")
