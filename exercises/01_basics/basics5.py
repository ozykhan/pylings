# basics5.py
#
# Integer maths. `/` always gives a float. `//` is floor division and
# `%` is the remainder that goes with it.
#
# Careful: Python floors toward negative infinity, JavaScript truncates
# toward zero. So -7 // 2 is -4 in Python and -3 in JS, and -7 % 2 is 1
# in Python and -1 in JS. Python's version is the one that makes clock
# arithmetic work.
#
# `divmod(a, b)` gives you both results at once as a tuple.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def split_seconds(total: int) -> tuple[int, int]:
    # Turn a number of seconds into (minutes, seconds).

    return divmod(total, 60)


# --- checks (do not edit) ------------------------------------------
eq(split_seconds(0), (0, 0))
eq(split_seconds(59), (0, 59))
eq(split_seconds(60), (1, 0))
eq(split_seconds(125), (2, 5))
eq(split_seconds(3600), (60, 0))

# Demonstrations, not tasks -- these already pass. Read them.
eq(7 / 2, 3.5, "/ always produces a float")
eq(7 // 2, 3, "// floors")
eq(-7 // 2, -4, "floors toward negative infinity, unlike JavaScript")
eq(-7 % 2, 1, "the remainder follows the same convention")
