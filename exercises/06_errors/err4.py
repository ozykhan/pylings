# err4.py
#
# When you catch a low-level failure and re-raise something meaningful,
# keep the original attached:
#
#     raise ConfigError(...) from exc
#
# The traceback then shows both, joined by "The above exception was the
# direct cause of the following exception". Without `from`, Python
# still shows the original but describes it as an accident
# ("During handling of the above exception, another occurred").
#
# `raise X from None` deliberately hides the original. Use it rarely.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq, ok, raises

class ConfigError(Exception):
    pass


def load_port(raw: str) -> int:
    # Parse raw as an int. On failure raise
    # ConfigError(f"bad port: {raw!r}") with the original ValueError
    # attached as its cause.
    ...


# --- checks (do not edit) ------------------------------------------
eq(load_port("8080"), 8080)

err = raises(ConfigError, lambda: load_port("http"))
eq(str(err), "bad port: 'http'")
ok(isinstance(err.__cause__, ValueError), "use `from exc` to set __cause__")
