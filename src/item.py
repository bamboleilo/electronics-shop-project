import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
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
        res = str(self.__class__).split('.')[-1][:-2]
        return f"{res}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

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
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """
        Класс-метод, инициализирующий экземпляры класса Item
        данными из файла src/items.csv
        """

        with open(file_name) as file:
            res = csv.DictReader(file)
            for i in res:
                if list(i.keys()) == ['name', 'price', 'quantity']:
                    cls(i['name'], i['price'], i['quantity'])

    @staticmethod
    def string_to_number(value):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(value))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")

