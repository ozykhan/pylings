# basics5.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def split_seconds(total: int) -> tuple[int, int]:
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
