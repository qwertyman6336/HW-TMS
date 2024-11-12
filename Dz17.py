# Задание 1
try:
    weight = float(input('Введите свой вес (кг): '))
    height = float(input('Введите свой рост (см): '))

    imt = (weight / (height ** 2)) * 10000

    if imt <= 16:
        print('Значительный дефицит массы тела')
    else:
        if imt <= 16 or imt <= 18.5:
            print('Недостаток массы тела')
        else:
            if imt <= 18.5 or imt <= 25:
                print('Норма')
            else:
                if imt <= 25 or imt <= 30:
                    print('Избыточная масса тела (предожирение)')
                else:
                    if imt <= 30 or imt <= 35:
                        print('Ожирение первой степени')
                    else:
                        if imt <= 35 or imt <= 40:
                            print('Ожирение второй степени')
                        else:
                            if imt <= 40 or imt <= 10000000:
                                print('Ожирение третьей степени (морбидное)')

except ZeroDivisionError:
    print('Нельзя делить на 0, ты явно выше чем 0;)')
except ValueError:
    print('Тут можно вводить только цифры, 0,1,2,3,4,5,6,7,8,9')
print('Спасибо что использовали мою программу;)')

# Задание 2

def calc( operation, a, b ):
    match operation:
        case '+': return a + b
        case '-': return a - b
        case '*': return a * b
        case '**': return a ** b
        case '/':
            try:
                return a / b
            except ZeroDivisionError:
                print('Нельзя делить на ноль')

while True:
    print()
    operation = input('Введите операцию (+, -, *, /,**, 0-завершение работы): ')
    if operation == '0':
        break
    if operation in '+-*/**':
        while True:
            try:
                a, b = map(float, input( 'Введите числа a, b через пробел = ' ).split())
                print(calc(operation,a,b))
                break
            except ValueError:
                print('Тут можно вводить только цифры')
                pass
