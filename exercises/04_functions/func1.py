# func1.py
#
# Parameters can have defaults, and callers can pass arguments by name
# in any order:
#
#     def f(a, b=2, c=3): ...
#     f(1, c=9)
#
# Named arguments at the call site are ordinary Python, not a special
# options-object pattern. Use them freely -- f(timeout=5) reads better
# than f(5).
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq

def make_url(host: str, path, scheme) -> str:
    # TODO: give path the default "/" and scheme the default "https"
    return ...


# --- checks (do not edit) ------------------------------------------
eq(make_url("example.com"), "https://example.com/")
eq(make_url("example.com", "/docs"), "https://example.com/docs")
eq(make_url("example.com", scheme="http"), "http://example.com/")
eq(make_url("example.com", "/a", "http"), "http://example.com/a")
eq(make_url(path="/x", host="example.com"), "https://example.com/x")
