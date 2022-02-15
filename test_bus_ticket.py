import bus
import pytest


def test_age_under_3():
    assert bus.ticket_price(2, 4) == 0


def test_age_under_19():
    assert bus.ticket_price(18, 4) == 2


def test_age_over_64():
    assert bus.ticket_price(65, 4) == 0