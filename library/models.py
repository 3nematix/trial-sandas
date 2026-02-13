import uuid
from dataclasses import dataclass
from enum import Enum


class BookStatus(Enum):
    AVAILABLE = "Available"
    BORROWED = "Borrowed"


@dataclass(frozen=True)
class Book:
    title: str
    author: str
    year: int


class BookCopy:
    def __init__(self, book: Book) -> None:
        self.id: uuid.UUID = uuid.uuid4()
        self.book: Book = book
        self.status: BookStatus = BookStatus.AVAILABLE

    def borrow(self) -> None:
        if self.status is BookStatus.BORROWED:
            raise ValueError("Book copy is already borrowed")
        self.status = BookStatus.BORROWED

    def return_copy(self) -> None:
        if self.status is BookStatus.AVAILABLE:
            raise ValueError("Book copy is already available")
        self.status = BookStatus.AVAILABLE

    def __repr__(self) -> str:
        return (
            f"BookCopy(id={self.id!s:.8}, "
            f"book={self.book!r}, "
            f"status={self.status.value})"
        )
