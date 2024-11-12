vibor = input('Выбор перевода систем счисления 10-ая (1) 2-ая (2):')
if vibor == "1":
    chislo10 = int(input("Введите число в десятичной системе счисления!: "))
    chislo1 = ''
    while chislo10 > 0:
        chislo1 = str(chislo10 % 2) + chislo1
        chislo10 = chislo10 // 2
    print("Ответ в двоичной системе счисления: " + chislo1)
elif vibor == "2":
    chislo2 = input("Введите число в двоичной системе счисления!: ")
    try:
        chislo3 = int(chislo2, 2)
        print("Ответ в десятичной системе счисления: " + str(chislo3))
    except ValueError:
        print("Ошибка, введите число в 2-ой системе счисления!")
end = input("Нажмите Enter для закрытия программы.")
