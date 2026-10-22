# strings5.py -- reference solution
#
# There is usually more than one right answer. If yours differs and the checks
# pass, yours is fine.

from pylings_check import eq

def format_price(amount: float, currency: str) -> str:
    return f"{currency} {amount:,.2f}"


# --- checks (do not edit) ------------------------------------------
eq(format_price(1234.5, "USD"), "USD 1,234.50")
eq(format_price(0, "TRY"), "TRY 0.00")
eq(format_price(1000000, "EUR"), "EUR 1,000,000.00")
eq(format_price(9.999, "GBP"), "GBP 10.00", "the spec rounds for you")
