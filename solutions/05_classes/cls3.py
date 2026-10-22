# cls3.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, ok, not_ok

class Tag:
    def __init__(self, name: str) -> None:
        self.name = name.lower()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tag):
            return NotImplemented
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


# --- checks (do not edit) ------------------------------------------
ok(Tag("Python") == Tag("python"), "compared by value, case-insensitively")
not_ok(Tag("a") == Tag("b"))
not_ok(Tag("a") == "a", "a Tag is not equal to a plain string")
eq(hash(Tag("Python")), hash(Tag("python")), "equal objects must hash equal")
eq(len({Tag("A"), Tag("a"), Tag("b")}), 2, "sets rely on both methods")
eq({Tag("x"): 1}[Tag("X")], 1, "and so do dict keys")
