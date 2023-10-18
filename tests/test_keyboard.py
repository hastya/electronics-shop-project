from src.keyboard import Keyboard


def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    try:
        kb.language = 'CH'
        # если меняем на язык который не разрешён
        assert False, "Ожидается ValueError"
    except ValueError as e:
        assert str(e) == "AttributeError: property 'language' of 'Keyboard' object has no setter"
