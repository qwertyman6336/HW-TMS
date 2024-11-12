def cyclic_sequence(*args):
    while True:
        for item in args:
            yield item


def main():
    try:
        num_elements = int(input("Введите количество элементов для вывода: "))
        if num_elements <= 0:
            raise ValueError("Количество элементов должно быть положительным числом.")

        sequence = cyclic_sequence(1, 2, 3)
        for i in range(num_elements):
            print(next(sequence), end="-")
        print()

    except ValueError as e:
        print(f"Ошибка: {e}")
    except KeyboardInterrupt:
        print("\nВыполнение прервано пользователем.")

if __name__ == "__main__":
    main()
