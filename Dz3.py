class SuperStr(str):

    def is_repeatance(self, a):
        if not a:
            return False

        if len(self) % len(a) == 0:
            repeat_count = len(self) // len(a)
            return self == a * repeat_count
        return False


    def is_palindrom(self):
        clean_str = self.lower().replace(" ", "")
        return clean_str == clean_str[::-1]


if __name__ == "__main__":
    my_string = SuperStr("ababab")
    print("Текущая строка:", my_string)

    print(f"Проверка на многократное повторение ab: {my_string.is_repeatance("ab")}")
    print(f"Проверка на многократное повторение a: {my_string.is_repeatance("a")}")
    print(f"Проверка на многократное повторение пустая строка: {my_string.is_repeatance("")}")

    pal_string1 = SuperStr("Рвал дед лавр")
    pal_string2 = SuperStr("Не является палидромом")

    print(f"Проверка на палидромом:{pal_string1}, {pal_string1.is_palindrom()}")
    print(f"Проверка на палидромом:{pal_string2}, {pal_string2.is_palindrom()}")

    empty_string = SuperStr("")
    print(f"Проверка на палидромом пустой строки: {empty_string.is_palindrom()}")
