def validate_age(age):
    # range check for age
    if not (1 <= age <= 120):
        raise ValueError(" Normal Insaan : 1->120")
    return True

def validate_price(price):
    # Non-negative check
    if price < 0:
        raise ValueError("Negative price not allowed")
    return True