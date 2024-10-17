import csv
import sys
from src.Errors import InstantiateCSVError
sys.path.insert(0, '..')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError
    
    @property
    def name(self) -> str:
        """
        :return: Название конкретного товара.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Изменяет название конкретного товара.

        :param value: Новое название.
        """
        if len(name) > 10:
            self.__name = name[0:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, filename):
        if filename[-9:] != 'items.csv':
            raise FileNotFoundError('_Отсутствует файл items.csv_')
        else:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError('_Файл item.csv поврежден_')
                    else:
                        Item(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string_number):
        float_number = float(string_number)
        int_number = int(float_number)
        return int_number

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price
