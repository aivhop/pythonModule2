class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError(f'Invalid data type for the name argument: {type(name)}, required type: str')
        if len(name.strip()) == 0:
            raise ValueError("The name of the book is incorrect, it cannot be empty")
        self._name = name

        if not isinstance(author, str):
            raise TypeError(f'Invalid data type for the author argument: {type(author)}, required type: str')
        if len(author.strip()) == 0:
            raise ValueError("The author of the book is incorrect, it cannot be empty")
        self._author = author

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.check_pages(pages)
        self._pages = pages

    def __str__(self) -> str:
        return f'Бумажная {super().__str__()}. Количество страниц {self._pages}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        self.check_pages(pages)
        self._pages = pages

    @staticmethod
    def check_pages(pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError(f'Invalid data type for the pages argument: {type(pages)}, required type: int')
        if pages < 1:
            raise ValueError("The number of pages is incorrect, it must be a positive number")


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.check_duration(duration)
        self._duration = duration

    def __str__(self) -> str:
        return f'Аудио {super().__str__()}. Продолжительность {self._duration}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        self.check_duration(duration)
        self._duration = duration

    @staticmethod
    def check_duration(duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError(f'Invalid data type for the duration argument: {type(duration)}, required type: float')
        if duration <= 0:
            raise ValueError("The duration value is incorrect, it must be a positive number")
