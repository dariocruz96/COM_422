import pytest
import Bus


def test_ticket_price():
    assert Bus.ticket_price(2, None, 4) == 0
    assert Bus.ticket_price(18, True, 4) == 2
    assert Bus.ticket_price(65, None, 4) == 0
    assert Bus.ticket_price(34, False, 4) == 4


# (speed, speed_limit)
def test_speeding_ticket():
    assert Bus.speeding_ticket(90, 100) == (False, False)
    assert Bus.speeding_ticket(90, 80) == (True, False)
    assert Bus.speeding_ticket(90, 70) == (True, True)


# 10 miles and over £100
def test_delivery_price():
    assert Bus.delivery_price(10, 100) == 0
    assert Bus.delivery_price(10, 90) == 5
    assert Bus.delivery_price(15, 150) == 10
    assert Bus.delivery_price(21, 150) == 15
    assert Bus.delivery_price(31, 150) == 15.5
