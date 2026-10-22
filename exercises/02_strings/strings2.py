# strings2.py
#
# `text.split()` with no arguments splits on any run of whitespace and
# drops empty pieces -- which is different from `split(" ")`. And
# `"-".join(parts)` is the reverse: separator first, then the pieces.
#
# `join` being a method on the separator surprises everyone at first.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def slugify(title: str) -> str:
    # Lowercase, and join the words with single hyphens.
    # Runs of whitespace count as one separator.
    return "-".join(title.lower().split())


# --- checks (do not edit) ------------------------------------------
eq(slugify("Hello World"), "hello-world")
eq(slugify("Hello   World  Again"), "hello-world-again")
eq(slugify("  Leading and trailing  "), "leading-and-trailing")
eq(slugify("Single"), "single")
eq(slugify(""), "")

# Demonstration: the no-argument form is the one you almost always want.
eq("a  b".split(), ["a", "b"])
eq("a  b".split(" "), ["a", "", "b"], "splitting on a literal space keeps the gap")
