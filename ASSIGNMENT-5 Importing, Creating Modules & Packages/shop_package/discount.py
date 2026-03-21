# the multiplier first to determine the remaining value after the percentage is shaved off.
def apply_discount(price, percent):
    return price * (1- percent / 100)

# direct fixed discount application
def flat_discount(price):
    return price - 50