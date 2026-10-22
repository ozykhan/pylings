# typ5.py
#
# A Protocol describes a shape. Any class with matching members
# satisfies it -- no inheritance, no registration. This is the
# structural typing you are used to from TypeScript interfaces, and it
# is the right tool for "anything with a .close() method".
#
# Add @runtime_checkable and isinstance() starts working too, though
# it only checks that the method names exist, not their signatures.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import ok, not_ok

from typing import Protocol, runtime_checkable


# TODO: a runtime-checkable Protocol named Closeable describing
#       anything with a close() method taking no arguments.
class Closeable:
    ...


# --- checks (do not edit) ------------------------------------------
class Socket:
    def close(self) -> None:
        pass


class Rock:
    pass


ok(isinstance(Socket(), Closeable), "Socket has close(), so it fits the shape")
not_ok(isinstance(Rock(), Closeable))
not_ok(issubclass(Socket, Rock), "and it inherits from nothing")
ok(issubclass(Socket, Closeable), "structural, not nominal")
