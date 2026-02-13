import pytest

from library.library import Library
from library.models import Book, BookCopy, BookStatus


@pytest.fixture
def lib():
    return Library()


@pytest.fixture
def sample_book():
    return Book(title="Dievų miškas", author="Balys Sruoga", year=1957)


class TestCreateBook:
    def test_creates_book(self, lib):
        book = lib.create_book("Dievų miškas", "Balys Sruoga", 1957)
        assert isinstance(book, Book)
        assert book.title == "Dievų miškas"
        assert book.author == "Balys Sruoga"
        assert book.year == 1957


class TestAddBook:
    def test_adds_copy(self, lib, sample_book):
        copy = lib.add_book(sample_book)
        assert isinstance(copy, BookCopy)
        assert copy.book == sample_book
        assert copy.status is BookStatus.AVAILABLE

    def test_multiple_copies(self, lib, sample_book):
        copy1 = lib.add_book(sample_book)
        copy2 = lib.add_book(sample_book)
        assert copy1.id != copy2.id


class TestBorrowBook:
    def test_borrow(self, lib, sample_book):
        lib.add_book(sample_book)
        borrowed = lib.borrow_book(sample_book)
        assert borrowed.status is BookStatus.BORROWED

    def test_borrow_picks_available_copy(self, lib, sample_book):
        copy1 = lib.add_book(sample_book)
        lib.add_book(sample_book)
        borrowed = lib.borrow_book(sample_book)
        assert borrowed.id == copy1.id
        assert borrowed.status is BookStatus.BORROWED

    def test_borrow_none_available(self, lib, sample_book):
        lib.add_book(sample_book)
        lib.borrow_book(sample_book)
        with pytest.raises(ValueError, match="No available copies"):
            lib.borrow_book(sample_book)

    def test_borrow_no_copies(self, lib, sample_book):
        with pytest.raises(ValueError, match="No available copies"):
            lib.borrow_book(sample_book)


class TestReturnBook:
    def test_return(self, lib, sample_book):
        lib.add_book(sample_book)
        borrowed = lib.borrow_book(sample_book)
        lib.return_book(borrowed)
        assert borrowed.status is BookStatus.AVAILABLE

    def test_return_already_available(self, lib, sample_book):
        copy = lib.add_book(sample_book)
        with pytest.raises(ValueError, match="already available"):
            lib.return_book(copy)

    def test_return_unknown_copy(self, lib, sample_book):
        foreign_copy = BookCopy(sample_book)
        with pytest.raises(ValueError, match="does not belong"):
            lib.return_book(foreign_copy)


class TestSearch:
    def test_search_by_title(self, lib):
        book = lib.create_book("Dievų miškas", "Balys Sruoga", 1957)
        lib.add_book(book)
        results = lib.search("Dievų miškas")
        assert len(results) == 1
        assert results[0].book == book

    def test_search_by_author(self, lib):
        book = lib.create_book("Dievų miškas", "Balys Sruoga", 1957)
        lib.add_book(book)
        results = lib.search("Balys Sruoga")
        assert len(results) == 1

    def test_search_no_results(self, lib):
        results = lib.search("Nežinoma knyga")
        assert results == []

    def test_search_deduplicates(self, lib):
        book = lib.create_book("Dievų miškas", "Balys Sruoga", 1957)
        lib.add_book(book)
        lib.add_book(book)
        lib.add_book(book)
        results = lib.search("Dievų miškas")
        assert len(results) == 1

    def test_search_sorted_newest_first(self, lib):
        old = lib.create_book("Anykščių šilelis", "Antanas Baranauskas", 1858)
        mid = lib.create_book("Altorių šešėly", "Vincas Mykolaitis-Putinas", 1933)
        new = lib.create_book("Dievų miškas", "Balys Sruoga", 1957)
        lib.add_book(old)
        lib.add_book(mid)
        lib.add_book(new)
        # All three have different authors, search won't return them together.
        # Instead, test sort with same-author books in TestSearch below.
        # Here just verify single results come back.
        assert lib.search("Balys Sruoga")[0].book.year == 1957

    def test_search_multiple_books_same_author_sorted(self, lib):
        book1 = lib.create_book("Senoji knyga", "Jonas Jonaitis", 1990)
        book2 = lib.create_book("Naujoji knyga", "Jonas Jonaitis", 2020)
        lib.add_book(book1)
        lib.add_book(book2)
        results = lib.search("Jonas Jonaitis")
        assert len(results) == 2
        assert results[0].book.year == 2020
        assert results[1].book.year == 1990
