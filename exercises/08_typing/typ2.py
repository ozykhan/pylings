# typ2.py
#
# A value that may be missing is written `int | None`. The older
# spelling is Optional[int]; they mean the same thing and the | form
# is preferred now.
#
# Optional does NOT mean "this argument can be left out" -- it means
# "None is one of the allowed values". A parameter is made optional by
# giving it a default, which is a separate thing.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

def find_score(scores: dict[str, int], name: str):
    # TODO: annotate the return type. It can return None.
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
