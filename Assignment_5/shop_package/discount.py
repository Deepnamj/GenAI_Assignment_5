def apply_discount(price, percent):
    disc = price * (percent / 100)
    return price - disc

def flat_discount(price):
    return price - 50
