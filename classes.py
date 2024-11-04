from dataclasses import dataclass
from typing import List, Union

class InvalidBookDataError(Exception):
    pass

@dataclass
class Book:
    book_id: int = None
    pages: int = 0
    year: int = 0
    author: str = ""
    price: float = 0.0

    def __post_init__(self):
        if not isinstance(self.pages, int) or self.pages <= 0:
            raise InvalidBookDataError("Количество страниц должно быть положительным целым числом.")
        if not isinstance(self.year, int) or self.year <= 0:
            raise InvalidBookDataError("Год издания должен быть положительным целым числом.")
        if not isinstance(self.author, str) or not self.author.strip():
            raise InvalidBookDataError("Автор должен быть указан.")
        if not isinstance(self.price, (int, float)) or self.price <= 0:
            raise InvalidBookDataError("Цена должна быть положительным числом.")

    def __lt__(self, other):
        return self.price < other.price

    def __str__(self):
        return (f"Книга(id={self.book_id}, Автор='{self.author}', Год написания={self.year},"
                f" Количество страниц={self.pages}, Цена={self.price:.2f})")


class Library:
    def __init__(self):
        self.books = []
        self.next_book_id = 1

    def add_book(self, book: Book):
        book.book_id = self.next_book_id
        self.next_book_id += 1
        self.books.append(book)

    def get_book_info(self, book_id: int) -> Union[Book, None]:
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_books_by_author(self, author: Union[str, List[str]]) -> List[Book]:
        if isinstance(author, str):
            author = [author]
        result = []
        for book in self.books:
            if book.author in author:
                result.append(book)
        return result

    def __str__(self):
        return f"Библиотека содержит {len(self.books)} книг."