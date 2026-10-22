# strings2.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def slugify(title: str) -> str:
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
