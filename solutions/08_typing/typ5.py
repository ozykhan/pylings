# typ5.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import ok, not_ok

from typing import Protocol, runtime_checkable


@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None: ...


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
