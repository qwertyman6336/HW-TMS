# Задание 1
numbers = [1, 2, 3, 4, 5]

strings = list(map(str,numbers))
print(strings)

# Задание 2
print(list(filter(lambda x: x>0 ,[0,10,20,30,1,2,3,4,5,6,7,8,9,0])))

# Задание 3
palindrom = str(input('Введите фразу для определения палиндрома: '))
palindrom = list(filter(str.isalpha, palindrom.casefold()))

if palindrom == palindrom [::-1]:
    print('Палиндром')
else:
    print('Не палиндром')
# Задание 4
import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        print(f"Время выполнения функции '{func.__name__}': {duration.total_seconds()} секунд")
        return result
    return wrapper
@timer
def my_function():
    print("Hello world!")
my_function()

# Задание 5
from functools import reduce
from operator import __add__

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

print(f'Площадь квартиры: {reduce(__add__,list(map(lambda x: x['length']*x['width'], rooms)))}м2')
