# basics3.py
#
# Now the trap that follows from basics2.
#
# `if not port:` is True for None *and* for 0. If 0 is a legitimate
# value, that check silently throws it away. The fix is to ask the
# question you actually mean: `if port is None:`.
#
# This is the single most common bug when people carry JavaScript
# habits over -- it is the same class of mistake as using || instead
# of ?? for defaults.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def resolve_port(port: int | None) -> int:
    # Return 8080 when no port was given.
    # But 0 is a real value a caller might pass, so keep it.
    if port is None:
        return 8080

    return port


# --- checks (do not edit) ------------------------------------------
eq(resolve_port(None), 8080, "no port given -> the default")
eq(resolve_port(0), 0, "0 was given explicitly -- do not replace it")
eq(resolve_port(3000), 3000)
