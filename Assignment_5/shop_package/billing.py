def calculate_total(prices):
    return sum(prices)

def apply_tax(amount):
    tax_amnt = amount * (5 / 100)
    return amount + tax_amnt