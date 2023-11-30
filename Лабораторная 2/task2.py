BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    },
    {
        "id": 4,
        "name": "Смешная книжка",
        "pages": 666,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным числом")
        self.id_ = id_
        self.name = name
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть положительным числом")
        self.pages = pages

    def __str__(self):
        return f"Книга \"{self.name}\""

    def __repr__(self):
        return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"

    def get_id(self) -> int:
        """Получение id книги"""
        return self.id_


class Library:
    def __init__(self, books: list['Book'] = None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку"""
        len_books = len(self.books)
        if len_books > 0:
            return len_books + 1
        else:
            return 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса"""
        for index, book in enumerate(self.books):
            if book_id == book.get_id():
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__

    print("=============================================")

    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

    print(library_with_books.get_index_by_book_id(2))  # проверяем индекс книги с id = 2

    try:
        print(library_with_books.get_index_by_book_id(3))  # проверяем индекс книги с id = 3
    except ValueError as e:
        print(f"> Исключение: {e}")

    print(library_with_books.get_index_by_book_id(4))  # проверяем индекс книги с id = 4
