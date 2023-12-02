class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга: {self._name}. Автор: {self._author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    """ Бумажная книга. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if self.pages_check(pages):
            self._pages = pages

    def __str__(self):
        parent_string = super().__str__()
        return f"{parent_string} Кол-во страниц: {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"

    @staticmethod
    def pages_check(value) -> bool:
        """Метод валидации значения кол-ва страниц книги"""
        if not isinstance(value, int):
            raise TypeError("Количество страниц книги должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц книги должно быть положителным числом.")
        return True

    @property
    def pages(self) -> int:
        return self._pages


class AudioBook(Book):
    """ Аудиокнига. """
    def __init__(self, name: str, author: str, duration: int | float):
        super().__init__(name, author)
        if self.duration_check(duration):
            self._duration = duration

    def __str__(self):
        parent_string = super().__str__()
        return f"{parent_string} Продолжительность: {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"

    @staticmethod
    def duration_check(value) -> bool:
        """Метод валидации значения продолжительности аудиокниги"""
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность аудиокниги должна быть целым или дробным числом.")
        if value <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом.")
        return True

    @property
    def duration(self) -> int | float:
        return self._duration


if __name__ == '__main__':
    book = Book("All about Common Books", "Common Brockie")
    paper_book = PaperBook("All about Paper Books", "Paper Brockie Jr", 812)
    audio_book = AudioBook("All about Audio Books", "Audin Brockie Jr", 52.7)
    multi_library = [book, paper_book, audio_book]

    for obj in multi_library:
        print(f"\n========={obj.__class__}=========")
        print(f"__str__: {str(obj)}")
        print(f"__repr__: {repr(obj)}")
        print(f"'name': {obj.name}")
        print(f"'author': {obj.author}")

        if isinstance(obj, PaperBook):
            print(f"'pages': {obj.pages}")
        if isinstance(obj, AudioBook):
            print(f"'duration': {obj.duration}")

    print(f"\n========= raise tests =========")
    try:
        paper_error_book = PaperBook("...", "...", "812")
    except TypeError as e:
        print(e)
    try:
        audio_error_book = AudioBook("...", "...", -52.0)
    except ValueError as e:
        print(e)
