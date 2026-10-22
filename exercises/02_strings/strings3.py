# strings3.py
#
# Slicing: text[start:stop], stop is exclusive, negative indices count
# from the end, and out-of-range slices do not raise -- they just give
# you what exists.
#
# One trap: text[-0:] is text[0:], the whole string, because -0 == 0.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def last_n(text: str, n: int) -> str:
    # The last n characters. If the string is shorter, return all of it.
    return text[-n:]


def without_ends(text: str) -> str:
    # Everything except the first and last character.
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
