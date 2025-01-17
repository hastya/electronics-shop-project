import csv

class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "Файл item.csv поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.name = name  # Название товара
        self.price = price  # Цена за единицу товара
        self.quantity = quantity  # Количество товара в магазине
        self.all.append(self)

    def __repr__(self):
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            return ValueError
        return self.quantity + other.quantity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        try:
            cls.all = []
            with open('../src/items.csv', newline='', encoding='Windows-1251') as f:
                read = csv.DictReader(f)
                for x in read:
                    name = x["name"]
                    price = x["price"]
                    quantity = x["quantity"]
                    if name is None or price is None or quantity is None:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except InstantiateCSVError as m:
            print(m.message)


    @staticmethod
    def string_to_number(string: str):
        x = float(string)
        return int(x)

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине"""
        return f"{self.price * self.quantity}"  # Общая стоимость товара

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара"""
        self.price *= self.pay_rate
