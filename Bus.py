def ticket_price(age, student, price):
    if age < 3:
        return 0
    elif age < 19 and student:
        return price / 2
    elif age > 64:
        return 0
    else:
        return price


def speeding_ticket(speed, speed_limit):
    if 0 < speed - speed_limit <= 10:
        ticket = True
        court = False
    elif 10 < speed - speed_limit:
        ticket = True
        court = True
    else:
        ticket = False
        court = False

    return ticket, court


def delivery_price(distance, value):
    price = 0
    if distance <= 10 and value >= 100:
        price = 0
    elif distance <= 10 and value < 100:
        price = 5
    elif 20 >= distance > 10:
        price = 10
    elif 30 >= distance > 20:
        price = 15
    elif distance > 30:
        price = 15 + (distance - 30)*0.5
    return price
