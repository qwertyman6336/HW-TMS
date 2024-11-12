# 1 задание
a = int(input('Первое число = '))
b = int(input('Второе число = '))
c = int(input('Третье число = '))
print(f"Cумма = {a + b + c}")
print(f"Разность = {a - b - c}")
print(f"Произведение = {a * b * c}")
print(f"От первой переменной отняли вторую и прибавили третью = {a - b + c}")
print(f"Поделили произведение двух переменных на третью = {(a + b) / c}")
print(f"От суммы первых двух переменных нашли остаток от деления на третью переменную = {(a + b) % c}")

# 2 задание
import math
cat_a = int(input('Первый катет = '))
cat_b = int(input('Второй катет = '))
hypotenuse = (cat_a**2 + cat_b**2)
square = ((cat_a * cat_b) / 2)
a = a = math.sqrt(hypotenuse)
print(f"Гипотенуза = {a}")
print(f"Площадь = {square}")

# задание 3
string = ('Hello world', 'a b c', 'test', 'test1 test2 test3 test4 test5')
print(f'Количество слов в строчке = {len(string)}')

# задание 4
string = ('hhhabchghhh')
print(f'Замена h на H = {string.replace('h','H', string.count('h')-1).replace('H','h',1)}'

# задание 5
word = ('Hello')
print(f'Третий сисмвол = {word [2] }')
print(f'Предпоследний символ строки = {word [-2] }')
print(f'Первые 5 символов строки = {word [0:5]}')
print(f'Все символы, кроме 2-х последних = {word [0:-2]}')
print(f'Все символы с чётными индексами = {word [::2]}')
print(f'Все символы с нечётными индексами = {word [1::2]}')
print(f'Все символы строки в обратном порядке = {word [::-1]}')
print(f'Все символы через один в обратном порядке, начиная с последнего = {word [::-2]}')
print(f'Длина всей строки = {len(word)}')

word = ('TEST-STR')
print(f'Третий сисмвол = {word [2] }')
print(f'Предпоследний символ строки = {word [-2] }')
print(f'Первые 5 символов строки = {word [0:5]}')
print(f'Все символы, кроме 2-х последних = {word [0:-2]}')
print(f'Все символы с чётными индексами = {word [::2]}')
print(f'Все символы с нечётными индексами = {word [1::2]}')
print(f'Все символы строки в обратном порядке = {word [::-1]}')
print(f'Все символы через один в обратном порядке, начиная с последнего = {word [::-2]}')
print(f'Длина всей строки = {len(word)}')

# задание 6
word = ('123456789')
print(f'Последняя цифра числа = {word [-1] }')

# задание 7
word = ('123456789')
print(f'Количество десятков = {word [-2] }')

# задание 8
number = int(input('число = '))
sum = 0
while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10
print("Сумма:", sum)

end = input("Нажмите Enter для закрытия программы.")
