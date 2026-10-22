# typ6.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

from typing import NotRequired, TypedDict


class UserRow(TypedDict):
    id: int
    name: str
    email: NotRequired[str]


# --- checks (do not edit) ------------------------------------------
eq(UserRow.__required_keys__, frozenset({"id", "name"}))
eq(UserRow.__optional_keys__, frozenset({"email"}), "wrap email in NotRequired")
eq(UserRow.__annotations__["id"], int)
eq(UserRow.__annotations__["name"], str)

# At runtime it is just a dict -- no validation, no class instance.
row: UserRow = {"id": 1, "name": "faruk"}
eq(row["name"], "faruk")
eq(type(row), dict)
