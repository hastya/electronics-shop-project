from src.item import Item


class LanguageMixin:
    def __init__(self):
        self.language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"


# class Keyboard(Item, LanguageMixin):
#     def __init__(self, name: str, price: float, quantity: int, language="EN"):
#         super().__init__(name, price, quantity)
#         self.__language = language
class Keyboard(Item, LanguageMixin):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if value in ["EN", "RU"]:
            self.__language = value  # Fix the attribute name here
        else:
            raise ValueError("AttributeError: property 'language' of 'Keyboard' object has no setter")
