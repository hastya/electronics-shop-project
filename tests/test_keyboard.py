from src.keyboard import Keyboard
import pytest

# def test_keyboard():
#     kb = Keyboard('Dark Project KD87A', 9600, 5)
#     assert str(kb) == "Dark Project KD87A"
#
# def test_change_lang():
#     kb = Keyboard('Dark Project KD87A', 9600, 5)
#     assert str(kb.language) == "EN"
#     kb.change_lang()
#     assert str(kb.language) == "RU"
#     try:
#         kb.language = 'CH'
#         # если меняем на язык который не разрешён
#         assert False, "Ожидается ValueError"
#     except ValueError as e:
#         assert str(e) == "AttributeError: property 'language' of 'Keyboard' object has no setter"


@pytest.fixture()
def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test_init(test_keyboard):
    assert test_keyboard.name == 'Dark Project KD87A'
    assert test_keyboard.price == 9600
    assert test_keyboard.quantity == 5


def test_lang(test_keyboard):
    assert str(test_keyboard.language) == "EN"
    test_keyboard.change_lang()
    assert str(test_keyboard.language) == "RU"
    test_keyboard.change_lang()
    assert str(test_keyboard.language) == "EN"


def test_change_lang(test_keyboard):
    try:
        test_keyboard.language == "CH"
    except:
        return AttributeError