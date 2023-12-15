import doctest
from typing import List

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
    }
]


class Book:
    """A book containing information about the identifier, name, and number of pages"""

    def __init__(self, id_: int, name: str, pages: int):
        """
        The usual constructor of the book object
        :param id_: The number indicating the identifier
        :param name: The string containing the name of the book
        :param pages: The number indicating the number of pages in a book

        Examples:
        >>> book = Book(1, "White Fang", 300)

        >>> book1 = Book('1', "White Fang", 300)
        Traceback (most recent call last):
        ...
        TypeError: Invalid data type for the id_ argument: <class 'str'>, required type: int

        >>> book2 = Book(1, 1, 300)
        Traceback (most recent call last):
        ...
        TypeError: Invalid data type for the name argument: <class 'int'>, required type: str

        >>> book3 = Book(1, "   ", 300)
        Traceback (most recent call last):
        ...
        ValueError: The name of the book is incorrect, it cannot be empty

        >>> book = Book(1, "White Fang", "300")
        Traceback (most recent call last):
        ...
        TypeError: Invalid data type for the pages argument: <class 'str'>, required type: int

        >>> book = Book(1, "White Fang", 0)
        Traceback (most recent call last):
        ...
        ValueError: The number of pages is incorrect, it must be a positive number
        """
        if not isinstance(id_, int):
            raise TypeError(f'Invalid data type for the id_ argument: {type(id_)}, required type: int')
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError(f'Invalid data type for the name argument: {type(name)}, required type: str')
        if len(name.strip()) == 0:
            raise ValueError("The name of the book is incorrect, it cannot be empty")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError(f'Invalid data type for the pages argument: {type(pages)}, required type: int')
        if pages < 1:
            raise ValueError("The number of pages is incorrect, it must be a positive number")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library:
    """Library aggregating books"""

    def __init__(self, books: List[Book] = []):
        """
        The usual constructor of the library object
        :param books: The list containing books. Empty by default

        Examples:
        >>> library = Library()
        >>> library1 = Library([Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE])
        >>> library2 = Library([Book(1, "White Fang", 300)])
        >>> library3 = Library(())
        Traceback (most recent call last):
        ...
        TypeError: Invalid data type for the books argument: <class 'tuple'>, required type: list
        >>> library4 = Library([Book(1, "White Fang", 300), "incorrect data obj"])
        Traceback (most recent call last):
        ...
        TypeError: Invalid object type in the list : <class 'str'> on the index: 1, required type: Book
        """
        if not isinstance(books, list):
            raise TypeError(f'Invalid data type for the books argument: {type(books)}, required type: list')
        if len(books) != 0:
            for ind, book in enumerate(books):
                if not isinstance(book, Book):
                    raise TypeError(
                        f'Invalid object type in the list : {type(book)} on the index: {ind}, required type: Book')
        self.books = books

    def get_next_book_id(self) -> int:
        """
        A method that returns the id for adding a new book to the library.
        :return:  If there are no books in the library, then return 1.
                    If there are books, then return the ID of the last book increased by 1

        Examples:
        >>> library = Library()
        >>> library1 = Library([Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE])
        >>> library.get_next_book_id() # empty lib
        1
        >>> library1.get_next_book_id()
        3
        """
        return self.books[-1].id_ + 1 if len(self.books) != 0 else 1

    def get_index_by_book_id(self, id_: int) -> int:
        """
        A method that returns the index of the book in the list, which is stored in the attribute of an instance of the class.
        :param id_: The id of the book you are looking for
        :return: If the book exists, then return the index from the list.
                    If there is no book,
                     then cause a ValueError error with the message: "The book with the requested id does not exist"

        Examples:
        >>> library1 = Library([Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE])
        >>> library1.get_index_by_book_id(1)
        0
        >>> library1.get_index_by_book_id(10000)
        Traceback (most recent call last):
        ...
        ValueError: Книги с запрашиваемым id не существует
        """
        if not isinstance(id_, int):
            raise TypeError(f'Invalid data type for the id_ argument: {type(id_)}, required type: int')
        for ind, book in enumerate(self.books):
            if book.id_ == id_:
                return ind
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

    doctest.testmod()
