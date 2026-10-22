# typ1.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def repeat(text: str, times: int) -> str:
    return text * times


# --- checks (do not edit) ------------------------------------------
from typing import get_type_hints

eq(repeat("ab", 2), "abab")
eq(
    get_type_hints(repeat),
    {"text": str, "times": int, "return": str},
    "annotate both parameters and the return",
)

# Demonstration: nothing is enforced at runtime. Annotations describe
# intent to a checker; they do not validate.
eq(repeat([0], 2), [0, 0], "a list still works -- mypy is what would complain")
