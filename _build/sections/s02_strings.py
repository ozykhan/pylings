SECTION = "02_strings"

EXERCISES = [
    dict(
        name="strings1",
        intro="""
        Strings are immutable. Every method returns a new string rather than
        changing the one you called it on, so methods chain naturally.
        """,
        hint="""
        Two methods, chained: one removes surrounding whitespace, one
        lowercases. Order does not matter here.
            raw.strip().lower()
        """,
        stub="""
        def normalize_email(raw: str) -> str:
            # Trim surrounding whitespace and lowercase it.
            return ...
        """,
        solution="""
        def normalize_email(raw: str) -> str:
            return raw.strip().lower()
        """,
        checks="""
        eq(normalize_email("  Faruk@Example.COM "), "faruk@example.com")
        eq(normalize_email("a@b.com"), "a@b.com")
        eq(normalize_email("\\n  MiXeD@Case.Org\\t"), "mixed@case.org")
        """,
    ),
    dict(
        name="strings2",
        intro="""
        `text.split()` with no arguments splits on any run of whitespace and
        drops empty pieces -- which is different from `split(" ")`. And
        `"-".join(parts)` is the reverse: separator first, then the pieces.

        `join` being a method on the separator surprises everyone at first.
        """,
        hint="""
        Lowercase it, split it on whitespace with no argument, then join the
        pieces with a hyphen:
            "-".join(title.lower().split())
        """,
        stub="""
        def slugify(title: str) -> str:
            # Lowercase, and join the words with single hyphens.
            # Runs of whitespace count as one separator.
            return ...
        """,
        solution="""
        def slugify(title: str) -> str:
            return "-".join(title.lower().split())
        """,
        checks="""
        eq(slugify("Hello World"), "hello-world")
        eq(slugify("Hello   World  Again"), "hello-world-again")
        eq(slugify("  Leading and trailing  "), "leading-and-trailing")
        eq(slugify("Single"), "single")
        eq(slugify(""), "")

        # Demonstration: the no-argument form is the one you almost always want.
        eq("a  b".split(), ["a", "b"])
        eq("a  b".split(" "), ["a", "", "b"], "splitting on a literal space keeps the gap")
        """,
    ),
    dict(
        name="strings3",
        intro="""
        Slicing: text[start:stop], stop is exclusive, negative indices count
        from the end, and out-of-range slices do not raise -- they just give
        you what exists.

        One trap: text[-0:] is text[0:], the whole string, because -0 == 0.
        """,
        hint="""
        last_n: a negative start and an empty stop -> text[-n:]
        without_ends: start at 1, stop one before the end -> text[1:-1]
        """,
        stub="""
        def last_n(text: str, n: int) -> str:
            # The last n characters. If the string is shorter, return all of it.
            return ...


        def without_ends(text: str) -> str:
            # Everything except the first and last character.
            return ...
        """,
        solution="""
        def last_n(text: str, n: int) -> str:
            return text[-n:]


        def without_ends(text: str) -> str:
            return text[1:-1]
        """,
        checks="""
        eq(last_n("abcdef", 2), "ef")
        eq(last_n("abcdef", 6), "abcdef")
        eq(last_n("ab", 5), "ab", "an over-long slice does not raise")
        eq(without_ends("abcdef"), "bcde")
        eq(without_ends("ab"), "")
        eq(without_ends("a"), "")

        # Demonstration of the -0 trap mentioned above.
        eq("abc"[-0:], "abc", "not the empty string -- -0 is 0")
        """,
    ),
    dict(
        name="strings4",
        intro="""
        removeprefix / removesuffix strip an affix only if it is actually
        there, and leave the string alone otherwise. Before they existed
        people wrote `if s.startswith(p): s = s[len(p):]` and got the length
        wrong.
        """,
        hint="""
        Chain two removeprefix calls. Try the longer prefix first and think
        about why the order matters -- or rather, why here it does not.
        """,
        stub="""
        def strip_protocol(url: str) -> str:
            # Remove a leading http:// or https://.
            # Anything else is returned unchanged.
            return ...
        """,
        solution="""
        def strip_protocol(url: str) -> str:
            return url.removeprefix("https://").removeprefix("http://")
        """,
        checks="""
        eq(strip_protocol("https://example.com/a"), "example.com/a")
        eq(strip_protocol("http://example.com"), "example.com")
        eq(strip_protocol("ftp://example.com"), "ftp://example.com")
        eq(strip_protocol("example.com"), "example.com")
        eq(strip_protocol(""), "")
        """,
    ),
    dict(
        name="strings5",
        intro="""
        Inside an f-string, a colon starts a format spec:

            {value:.2f}    two decimal places
            {value:,}      thousands separators
            {value:>10}    right-align in 10 columns
            {value:08.3f}  zero-padded, 8 wide, 3 decimals

        This replaces most of what you would reach for toLocaleString or a
        formatting library for.
        """,
        hint="""
        One f-string. The spec you want combines a comma and two decimals:
            f"{currency} {amount:,.2f}"
        """,
        stub="""
        def format_price(amount: float, currency: str) -> str:
            # "USD 1,234.50" -- thousands separated, always two decimals.
            return ...
        """,
        solution="""
        def format_price(amount: float, currency: str) -> str:
            return f"{currency} {amount:,.2f}"
        """,
        checks="""
        eq(format_price(1234.5, "USD"), "USD 1,234.50")
        eq(format_price(0, "TRY"), "TRY 0.00")
        eq(format_price(1000000, "EUR"), "EUR 1,000,000.00")
        eq(format_price(9.999, "GBP"), "GBP 10.00", "the spec rounds for you")
        """,
    ),
    dict(
        name="strings6",
        intro="""
        A `str` is a sequence of characters. A `bytes` is a sequence of bytes.
        They are different types and Python will not quietly convert between
        them -- you encode a str to bytes and decode bytes back to a str.

        This matters the moment you touch a network, a file, or a Content-Length
        header, because len() of the two is not the same number.
        """,
        hint="""
        text.encode("utf-8") gives you a bytes object. Take its len().
        """,
        stub="""
        def byte_length(text: str) -> int:
            # How many BYTES this text takes in UTF-8 -- not how many characters.
            return ...
        """,
        solution="""
        def byte_length(text: str) -> int:
            return len(text.encode("utf-8"))
        """,
        checks="""
        eq(byte_length("abc"), 3)
        eq(byte_length(""), 0)
        eq(byte_length("ğ"), 2, "one character, two bytes")
        eq(byte_length("İstanbul"), 9, "eight characters, nine bytes")

        # Demonstration: the two lengths genuinely differ.
        eq(len("İstanbul"), 8)
        eq(type("a".encode()).__name__, "bytes")
        eq(b"abc".decode("utf-8"), "abc")
        """,
    ),
]
