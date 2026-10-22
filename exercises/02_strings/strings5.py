# strings5.py
#
# Inside an f-string, a colon starts a format spec:
#
#     {value:.2f}    two decimal places
#     {value:,}      thousands separators
#     {value:>10}    right-align in 10 columns
#     {value:08.3f}  zero-padded, 8 wide, 3 decimals
#
# This replaces most of what you would reach for toLocaleString or a
# formatting library for.
#
# Make the checks at the bottom pass.
# Stuck? Press `h` in pylings for a hint.

from pylings_check import eq


def format_price(amount: float, currency: str) -> str:
    # "USD 1,234.50" -- thousands separated, always two decimals.
    return f"{currency} {amount:,.2f}"


# --- checks (do not edit) ------------------------------------------
eq(format_price(1234.5, "USD"), "USD 1,234.50")
eq(format_price(0, "TRY"), "TRY 0.00")
eq(format_price(1000000, "EUR"), "EUR 1,000,000.00")
eq(format_price(9.999, "GBP"), "GBP 10.00", "the spec rounds for you")
