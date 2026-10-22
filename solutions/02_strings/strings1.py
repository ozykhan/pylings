# strings1.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def normalize_email(raw: str) -> str:
    return raw.strip().lower()


# --- checks (do not edit) ------------------------------------------
eq(normalize_email("  Faruk@Example.COM "), "faruk@example.com")
eq(normalize_email("a@b.com"), "a@b.com")
eq(normalize_email("\n  MiXeD@Case.Org\t"), "mixed@case.org")
