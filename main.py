from classes import Book, Library, InvalidBookDataError

try:
    library = Library()
    library.add_book(Book(pages=300, year=2020, author="Лев Толстой", price=25.50))
    library.add_book(Book(pages=200, year=2023, author="Сергей Есенин", price=15.00))
    library.add_book(Book(pages=400, year=2022, author="Лев Толстой", price=30.00))
    library.add_book(Book(pages=150, year=2021, author="Фёдор Достоевский", price=10.00))


    print(library)
    print(library.get_book_info(1))
    print(library.find_books_by_author("Лев Толстой"))
    print(library.find_books_by_author(["Лев Толстой", "Сергей Есенин"]))

    library.add_book(Book(pages=-100, year=2024, author="Author D", price=40.00))

except InvalidBookDataError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")