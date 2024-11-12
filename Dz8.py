# задание 2
k = int(input('Сколько откладывать = '))
N = int(input('Стоимость телефона = '))
day = 1
s = 0
while s < N:
    if day % 7 != 0:
        s = s + k
    day = day + 1
print(f'Сколько потребуется дней = {day - 1}')
# задание 3
fib1 = fib2 = 1
n = int(input('Напишите ряд Фибоначчи = '))
for i in range(1, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end = ', ')
# задание 4
list = [1,2,30,44,55,75,3,4,5,6,7,8,9,12,15,16,43,23,25,79,78,91,26]
print(f'Первое число списка {list[0]}')
print(f'Последнее число списка {list[-1]}')
print(f'Сумма списка чисел = {sum(list)}')
# задание 5
from random import randrange
N = 15
arr = [randrange(50) for i in range(N)]
print(*arr)
for item in arr:
    if arr.count(item) > 1:
        print("Есть одинаковые элементы")
        break
else:
    print("Все элементы уникальны")
# задание 6
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n= int(input('Число для поиска = '))
def bin_search(list, n):
    start = 0
    end = len(list)
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == n:
            return mid
        if n < list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
print(bin_search(list, n))
# Задание 1, 2 матрицы
def mat():
    n = int(input("Сколько столбцов?: "))
    spisok = [[0 for x in range(n)] for y in range(n)]
    k = 100
    for zapolnenie_stroki in range(n):
        for zapolnenie_elementa in range(n):
            spisok[zapolnenie_stroki][zapolnenie_elementa] = k
            k += 2
    for zapolnenie_stroki in range(n):
        for zapolnenie_elementa in range(n):
            print(spisok[zapolnenie_stroki][zapolnenie_elementa], end=' ')
        print()
mat()


# Задание 3 матрицы
matrix = [
    [1, 2, 3,],
    [4, 5, 6,],
    [7, 8, 9,]
]
zapolnenie_stroki = len(matrix)
zapolnenie_elementa = len(matrix[0])
new_matix = [[0] * zapolnenie_stroki for _ in range(zapolnenie_elementa)]
for i in range(zapolnenie_stroki):
    for j in range(zapolnenie_elementa):
        new_matix[j][i] = matrix[i][j]
for row in new_matix:
    print(row)
