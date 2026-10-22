# strings1.py
#
# Strings are immutable. Every method returns a new string rather than
# changing the one you called it on, so methods chain naturally.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def normalize_email(raw: str) -> str:
    # Trim surrounding whitespace and lowercase it.
    return raw.lower().strip()


# --- checks (do not edit) ------------------------------------------
eq(normalize_email("  Faruk@Example.COM "), "faruk@example.com")
eq(normalize_email("a@b.com"), "a@b.com")
eq(normalize_email("\n  MiXeD@Case.Org\t"), "mixed@case.org")
