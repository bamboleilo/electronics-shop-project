"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

item1 = Item("Смартфон", 10000, 5)
item2 = Item("Ноутбук", 50000, 2)
Item.pay_rate = 0.9
def test_calculate_total_price():
    '''
    Тест на проверку функции get_filtered_data на количество значений EXECUTED
    '''
    print()
    assert item1.calculate_total_price() == 50000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    '''
    Тест на проверку функции get_filtered_data на количество значений EXECUTED
    '''
    assert item1.apply_discount() == 45000
    assert item2.apply_discount() == 90000

