# cls3.py
#
# By default two objects are equal only if they are the same object.
# Define __eq__ to compare by value instead.
#
# The moment you define __eq__, Python sets __hash__ to None and your
# class becomes unusable in a set or as a dict key. You must define
# __hash__ too, and the contract is: equal objects MUST have equal
# hashes. Hash whatever you compared.
#
# Returning NotImplemented (not False) for an unknown type lets Python
# try the other object's __eq__ before giving up.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, ok, not_ok

class Tag:
    def __init__(self, name: str) -> None:
        self.name = name.lower()

    def __eq__(self, other: object) -> bool:
        ...

    def __hash__(self) -> int:
        ...


# --- checks (do not edit) ------------------------------------------
ok(Tag("Python") == Tag("python"), "compared by value, case-insensitively")
not_ok(Tag("a") == Tag("b"))
not_ok(Tag("a") == "a", "a Tag is not equal to a plain string")
eq(hash(Tag("Python")), hash(Tag("python")), "equal objects must hash equal")
eq(len({Tag("A"), Tag("a"), Tag("b")}), 2, "sets rely on both methods")
eq({Tag("x"): 1}[Tag("X")], 1, "and so do dict keys")
