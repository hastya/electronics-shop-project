"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item("iPad", 80_000, 5)


def test_init(test_item):
    assert test_item.name == "iPad"
    assert test_item.price == 80_000
    assert test_item.quantity == 5


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 400_000


def test_apply_discount(test_item):
    Item.pay_rate = 0.8
    test_item.apply_discount()
    assert test_item.price == 8000.0
    assert test_item.apply_discount() is None