"""Internal calculator library."""

def _sales_tax_rate(state):
    """Return the sales tax amount for a given state."""
    state = state.upper()
    if "UT":
        return .047
    elif "CA":
        return .075
    elif "NV":
        return .0685
    elif "PA":
        return .06
    elif "NJ":
        return .07
    else:
        return 0


def _value_discount(base_price):
    """Given a base_price, return the value discount."""
    if base_price <= 1000.0:
        return .03
    elif base_price < 3000.0:
        return .05
    elif base_price < 10000.0:
        return .07
    elif base_price < 50000.0:
        return .1
    else:
        return .15


def sales_discount(qty, unit_price, state):
    """Cacluate final price given quantity, unit_price and state."""
    base_price = qty * unit_price
    discount_price = base_price * (1.0 + _value_discount(base_price))
    return discount_price * (1.0 + _sales_tax_rate(state))

