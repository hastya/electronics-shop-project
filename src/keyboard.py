from src.item import Item

class LanguageMixin:

    def __init__(self):
        """Инциализации с языком по умолчанию EN."""
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self) -> None:
        """Метод для смены языка"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


    @language.setter
    def language(self, value):
        if value in ["EN", "RU"]:
            self.__language = value  # Fix the attribute name here
        else:
            raise ValueError("AttributeError: property 'language' of 'Keyboard' object has no setter")


# class Keyboard(Item, LanguageMixin):
#     def __init__(self, name: str, price: float, quantity: int, language="EN"):
#         super().__init__(name, price, quantity)
#         self.__language = language
class Keyboard(Item, LanguageMixin):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)
