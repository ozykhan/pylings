# strings3.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def last_n(text: str, n: int) -> str:
    return text[-n:]


def without_ends(text: str) -> str:
    return text[1:-1]


# --- checks (do not edit) ------------------------------------------
eq(last_n("abcdef", 2), "ef")
eq(last_n("abcdef", 6), "abcdef")
eq(last_n("ab", 5), "ab", "an over-long slice does not raise")
eq(without_ends("abcdef"), "bcde")
eq(without_ends("ab"), "")
eq(without_ends("a"), "")

# Demonstration of the -0 trap mentioned above.
eq("abc"[-0:], "abc", "not the empty string -- -0 is 0")
