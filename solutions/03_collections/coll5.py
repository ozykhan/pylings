# coll5.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def squares_of_evens(values: list[int]) -> list[int]:
    return [v * v for v in values if v % 2 == 0]


# --- checks (do not edit) ------------------------------------------
eq(squares_of_evens([1, 2, 3, 4]), [4, 16])
eq(squares_of_evens([]), [])
eq(squares_of_evens([1, 3, 5]), [])
eq(squares_of_evens([0, -2]), [0, 4])
