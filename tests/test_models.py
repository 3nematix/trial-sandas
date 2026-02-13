import pytest

from library.models import Book, BookCopy, BookStatus


class TestBookStatus:
    def test_values(self):
        assert BookStatus.AVAILABLE.value == "Available"
        assert BookStatus.BORROWED.value == "Borrowed"


class TestBook:
    def test_creation(self):
        book = Book(title="Altorių šešėly", author="Vincas Mykolaitis-Putinas", year=1933)
        assert book.title == "Altorių šešėly"
        assert book.author == "Vincas Mykolaitis-Putinas"
        assert book.year == 1933

    def test_equality(self):
        book1 = Book(title="Dievų miškas", author="Balys Sruoga", year=1957)
        book2 = Book(title="Dievų miškas", author="Balys Sruoga", year=1957)
        assert book1 == book2

    def test_inequality(self):
        book1 = Book(title="Dievų miškas", author="Balys Sruoga", year=1957)
        book2 = Book(title="Altorių šešėly", author="Vincas Mykolaitis-Putinas", year=1933)
        assert book1 != book2

    def test_frozen(self):
        book = Book(title="Dievų miškas", author="Balys Sruoga", year=1957)
        with pytest.raises(AttributeError):
            book.title = "Kitas pavadinimas"


class TestBookCopy:
    def test_creation_defaults_to_available(self):
        book = Book(title="Dievų miškas", author="Balys Sruoga", year=1957)
        copy = BookCopy(book)
        assert copy.book == book
        assert copy.status is BookStatus.AVAILABLE
        assert copy.id is not None

    def test_unique_ids(self):
        book = Book(title="Dievų miškas", author="Balys Sruoga", year=1957)
        copy1 = BookCopy(book)
        copy2 = BookCopy(book)
        assert copy1.id != copy2.id

    def test_borrow(self):
        copy = BookCopy(Book(title="Dievų miškas", author="Balys Sruoga", year=1957))
        copy.borrow()
        assert copy.status is BookStatus.BORROWED

    def test_borrow_already_borrowed(self):
        copy = BookCopy(Book(title="Dievų miškas", author="Balys Sruoga", year=1957))
        copy.borrow()
        with pytest.raises(ValueError, match="already borrowed"):
            copy.borrow()

    def test_return_copy(self):
        copy = BookCopy(Book(title="Dievų miškas", author="Balys Sruoga", year=1957))
        copy.borrow()
        copy.return_copy()
        assert copy.status is BookStatus.AVAILABLE

    def test_return_already_available(self):
        copy = BookCopy(Book(title="Dievų miškas", author="Balys Sruoga", year=1957))
        with pytest.raises(ValueError, match="already available"):
            copy.return_copy()
