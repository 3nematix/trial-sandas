from library.models import Book, BookCopy, BookStatus


class Library:
    def __init__(self) -> None:
        self._copies: list[BookCopy] = []

    def create_book(self, title: str, author: str, year: int) -> Book:
        return Book(title=title, author=author, year=year)

    def add_book(self, book: Book) -> BookCopy:
        copy = BookCopy(book)
        self._copies.append(copy)
        return copy

    def borrow_book(self, book: Book) -> BookCopy:
        for copy in self._copies:
            if copy.book == book and copy.status is BookStatus.AVAILABLE:
                copy.borrow()
                return copy
        raise ValueError(f"No available copies of {book.title!r}")

    def return_book(self, book_copy: BookCopy) -> None:
        if book_copy not in self._copies:
            raise ValueError("Book copy does not belong to this library")
        book_copy.return_copy()

    def search(self, query: str) -> list[BookCopy]:
        seen_books: set[Book] = set()
        results: list[BookCopy] = []
        for copy in self._copies:
            if copy.book in seen_books:
                continue
            if copy.book.title == query or copy.book.author == query:
                seen_books.add(copy.book)
                results.append(copy)
        results.sort(key=lambda c: c.book.year, reverse=True)
        return results
