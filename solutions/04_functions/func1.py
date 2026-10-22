# func1.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def make_url(host: str, path: str = "/", scheme: str = "https") -> str:
    return f"{scheme}://{host}{path}"


# --- checks (do not edit) ------------------------------------------
eq(make_url("example.com"), "https://example.com/")
eq(make_url("example.com", "/docs"), "https://example.com/docs")
eq(make_url("example.com", scheme="http"), "http://example.com/")
eq(make_url("example.com", "/a", "http"), "http://example.com/a")
eq(make_url(path="/x", host="example.com"), "https://example.com/x")
