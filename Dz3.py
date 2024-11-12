import math


# задание 1
a = int(input('a = '))
b = int(input('b = '))
print(f'y = {((a**2)/3) + ((a**2) + 4) / b + (math.sqrt((a**2) + 4)) / 4 + (math.sqrt(((a**2) + 4)) **3) / 4}')

x = int(input('x = '))
cos = math.cos(int(input('cos = ')))
sin = math.sin(int(input('sin = ')))
print(f'y = {math.cbrt ((cos**2) * (x**2) + (sin**2) * (2 * x - 1)) }')

cos = math.cos(int(input('cos = ')))
sin = math.sin(int(input('sin = ')))
print(f'y = {cos + sin}')

x = int(input('x = '))
sin = math.sin(int(input('sin = ')))
print(f'y = {5*x + 3 * (x**2) * math.sqrt(1 + (sin**2) * x) }')

# задание 2
i = int(input('Годовая процентная ставка: '))
s = int(input('Сумма займа: '))
n = int(input('Количество месяц, на который требуется кредит: '))
i = i/100
p = i/12
m = (s * p * ((1 + p) ** n)) / (((1 + p)**n)-1)
print(f'Ежемесячная сумма выплат по кредиту: {int(m)} бел.руб.')
print(f'Итоговая сумма выплат по кредиту: {int(m*n)} бел.руб.')
print(f'Переплаты составят: {int((m*n)-s)} бел.руб.')

# задание 3
R1 = float(input('Радиус орбиты планеты (млн.км.): '))
v1 = float(input('Орбитальная скорость (км/с): '))
R1 = R1 * 1000000
L1 = ((2 * R1 * math.pi) / v1 )
L1 = L1 / (60 * 60 * 24)
print(f'Длина года {int(L1)} дня')
R2 = float(input('Радиус орбиты планеты (млн.км.): '))
v2 = float(input('Орбитальная скорость (км/с): '))
R2 = R2 * 1000000
L2 = ((2 * R2 * math.pi) / v2 )
L2 = L2 / (60 * 60 * 24)
print(f'Длина года {int(L2)} дня')
if (L1 > L2):
    print(f'Длина года на первой планете {int(L1)} дня, а на второй {int(L2)} дня, следовательно год на первой планете больше чем на второй!')
elif (L1 < L2):
    print(f'Длина года на первой планете {int(L1)} дня, а на второй {int(L2)} дня, следовательно год на первой планете меньше чем на второй!')
end = input("Нажмите Enter для закрытия программы.")
