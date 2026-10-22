# typ2.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def find_score(scores: dict[str, int], name: str) -> int | None:
    return scores.get(name)


# --- checks (do not edit) ------------------------------------------
from typing import get_type_hints

eq(find_score({"a": 1}, "a"), 1)
eq(find_score({"a": 1}, "b"), None)
eq(
    get_type_hints(find_score)["return"],
    int | None,
    "the return type should be int | None",
)
