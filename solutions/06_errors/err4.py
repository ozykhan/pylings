# err4.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq, ok, raises

class ConfigError(Exception):
    pass


def load_port(raw: str) -> int:
    try:
        return int(raw)
    except ValueError as exc:
        raise ConfigError(f"bad port: {raw!r}") from exc


# --- checks (do not edit) ------------------------------------------
eq(load_port("8080"), 8080)

err = raises(ConfigError, lambda: load_port("http"))
eq(str(err), "bad port: 'http'")
ok(isinstance(err.__cause__, ValueError), "use `from exc` to set __cause__")
