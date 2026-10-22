# typ1.py
#
# Type hints are optional and Python does not enforce them at runtime.
# A checker like mypy reads them -- that is the whole point, the same
# split you have between tsc and the JavaScript that actually runs.
#
# Syntax: `name: type` for parameters, `-> type` for the return.
#
# These exercises verify your annotations with typing.get_type_hints,
# which reads them back at runtime, so you can see that they are real
# objects and not comments.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

def repeat(text, times):
    # TODO: annotate the parameters and the return type.
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
