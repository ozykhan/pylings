# typ6.py
#
# A TypedDict describes the shape of a dict whose keys are known --
# JSON payloads, rows from a database driver, config blobs. At runtime
# it is an ordinary dict with no overhead; the structure exists only
# for the checker.
#
# NotRequired[...] marks a key that may be absent. Reach for a
# dataclass when you control the data, and a TypedDict when you are
# describing a dict someone else's code hands you.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

from typing import NotRequired, TypedDict


# TODO: a TypedDict named UserRow with
#       id: int, name: str, and an optional email: str
class UserRow:
    ...


# --- checks (do not edit) ------------------------------------------
eq(UserRow.__required_keys__, frozenset({"id", "name"}))
eq(UserRow.__optional_keys__, frozenset({"email"}), "wrap email in NotRequired")
eq(UserRow.__annotations__["id"], int)
eq(UserRow.__annotations__["name"], str)

# At runtime it is just a dict -- no validation, no class instance.
row: UserRow = {"id": 1, "name": "faruk"}
eq(row["name"], "faruk")
eq(type(row), dict)
