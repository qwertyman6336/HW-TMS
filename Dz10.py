# Задание 1
list = [1,2,3,4,5,6,7,8,9,10]
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
print(bin_search(list, int(input('Введите искомое число = '))))
# Задание 2
decimal_number = int(input('Введите число в десячичной с/ч = '))
def find(decimal_number):
    if decimal_number == 0:
        return 0
    else:
        return (decimal_number % 2 + 10 * find(int(decimal_number // 2)))
print(find(decimal_number))
# Задание 3
number = int(input('Введите число = '))
def prime(number):
    if number == 2:
        return 'Простое число'
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return 'Составное число'
    return 'Простое число'
print(prime(number))
# Задание 4
a,b=map(int,input('Введите 2 числа через пробел = ').split())
def gcd(a,b):
    while b != 0:
        a, b = b,a % b
    return a
print(gcd(a,b))
# Задание 5
vibor = int(input('Для выбора режима работы шифра набери 1 для шифрования или 2 для дешифрования = '))
shag = int(input('Сдвиг шифра Цезаря = '))
text = input('Введите текст для шифрования = ')
s = set()
if vibor == 1:
    for i in range(len(text)):
        k = ord(text[i])
        l = k + shag
        print(chr(l), end='')
if vibor == 2:
    for i in range(len(text)):
        k = ord(text[i])
        l = k - shag
        print(chr(l), end='')
# Задание 7
import random
n = int(input('Число строк = '))
m = int(input('Число столбцов = '))
random_matrix = [[random.randint(1, 101) for e in range(n)] for e in range(m)]
for i in range(m):
    print(random_matrix[i])
# Задание 8
import random
n = int(input('Число строк = '))
m = int(input('Число столбцов = '))
random_matrix = [[random.randint(1, 101) for e in range(n)] for e in range(m)]
for i in range(m):
    print(random_matrix[i])
dup = []
for k in random_matrix:
    for i in k:
        dup.append(i)
print (f'''Максимальое число в матрице = {max(dup)}, 
Минималье число в матрице {min(dup)}''')
# Задание 9
import random
n = int(input('Число строк = '))
m = int(input('Число столбцов = '))
random_matrix = [[random.randint(1, 101) for e in range(n)] for e in range(m)]
for i in range(m):
    print(random_matrix[i])
dup = []
for k in random_matrix:
    for i in k:
        dup.append(i)
print (f'Сумма чисел в матрице = {sum(dup)}')
sum_col = [0] * m
for i in range(n):
    for j in range(m):
        sum_col[j] += random_matrix[i][j]
s = sum(sum_col)
for j in range(m):
    sum_col[j] = round(sum_col[j] / s, 3)
random_matrix.append(sum_col)
for row in random_matrix:
    print(*row)
# Задание 13
import random
n = int(input('Число строк = '))
m = int(input('Число столбцов = '))
random_matrix = [[random.randint(1, 10) for e in range(n)] for e in range(m)]
for i in range(m):
    print(random_matrix[i])
sum_first_diagonal = sum(random_matrix[i][i] for i in range(n))
sum_second_diagonal = sum(random_matrix[i][n - 1 - i] for i in range(n))
print(f'Сумма чисел главной диагонали = {str(sum_first_diagonal)}')
print(f'Сумма чисел вспомогательной диагонали = {str(sum_second_diagonal)}')
# Задание 12
import random
n = int(input('Число строк = '))
m = int(input('Число столбцов = '))
random_matrix = [[random.randint(1, 10) for e in range(n)] for e in range(m)]
for i in range(m):
    print(random_matrix[i])
H = int(input('Искомое число = '))
for num, column in enumerate(zip(*random_matrix)):
    if H in column:
        indices = [idx for idx, _ in enumerate(column) if _ == H]
        print('Столбец {} имеет {} ее индекс {}'.format(num, H, indices))
    else:
        print('Столбец {} не имеет {}'.format(num, H))
# Задание 14
import random
matrix = []
for i in range(3):
    row =[]
    for i in range(3):
        row.append(random.randint(0, 1))
    matrix.append(row)
    print(row)
print()
for row in matrix:
    if row.count(1) % 2 != 0:
        row.append(1)
    else:
        row.append(0)
    print(row)
