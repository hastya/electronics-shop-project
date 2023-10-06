"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
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


def test_name_setter(item):
    item.name = 'СуперСмартфон'
    assert item._name == "СуперСмарт"


def test_instantiate_from_csv():
    with open('../items.csv', encoding='cp1251') as file:
        read = csv.DictReader(file)
        assert read is not None
        for x in read:
            assert "name" in x
            assert "price" in x
            assert "quantity" in x


def test_instantiate_from_csv_error():
    assert Item.instantiate_from_csv() is None