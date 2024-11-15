from ast import Index
from itertools import product
from multiprocessing.managers import Value


class Product:
    def __init__(self, name, store, price):
        self.__name__ = name
        self.__store__ = store
        self.__price__ = price

    def get_name(self):
        return self.__name__

    def get_store(self):
        return self.__store__

    def get_price(self):
        return self.__price__

    def __str__(self):
        return f"Товар: {self.__name__},Магазин:{self.__store__},Цена:{self.__price__}"

class Warehouse:
    def __init__(self):
            self.__products = []

    def add_product(self, products):
            self.__products.append(products)

    def get_product_by_index(self, index):
        if 0 <= index < len(self.__products):
            return self.__products[index]
        raise IndexError("Индекс вне диапазона")

    def get_product_by_name(self, name):
        result = [product for product in self.__products if product.get_name().lower() == name.lower()]
        if result:
            return result
        raise ValueError("Товар не найден")

    def sort_by_name(self):
        self.__products.sort(key=lambda p: p.get_name())

    def sort_by_store(self):
        self.__products.sort(key=lambda p: p.get_store())

    def sort_by_price(self):
        self.__products.sort(key=lambda p: p.get_price())

    def __add__(self, other):
        if isinstance(other, Warehouse):
            total_price = sum(product.get_price() for product in self.__products) + \
                            sum(product.get_price() for product in other.__products)
            return total_price
        return NotImplemented

    def display_all_products(self):
        for product in self.__products:
            print(product)

if __name__ == "__main__":
    warehouse = Warehouse()

    product1 = Product("Хлеб", "Магазин 1", 30)
    product2 = Product("Молоко", "Магазин 2", 50)
    product3 = Product("Яблоки", "Магазин 1", 70)

    warehouse.add_product(product1)
    warehouse.add_product(product2)
    warehouse.add_product(product3)

    print("Все товары на складе:")
    warehouse.display_all_products()

    print("\nТовар по индексу 1:")
    print(warehouse.get_product_by_index(2))

    try:
        print("\nТовар по имени 'Хлеб':")
        print(warehouse.get_product_by_name("Хлеб"))
    except ValueError as e:
        print(e)

    print("\nСортировка по имени:")
    warehouse.sort_by_name()
    warehouse.display_all_products()

    print("\nСортировка по магазину:")
    warehouse.sort_by_store()
    warehouse.display_all_products()

    print("\nСортировка по цене:")
    warehouse.sort_by_price()
    warehouse.display_all_products()

    # Пример сложения цен от двух складов
    warehouse2 = Warehouse()
    warehouse2.add_product(Product("Сыр", "Магазин 3", 100))
    total_price = warehouse + warehouse2
    print(f"\nОбщая стоимость товаров на двух складах: {total_price} руб.")