def ticket_price(age, price):
    if age < 3:
        return 0
    elif age < 19:
        return price / 2
    elif age > 64:
        return 0
