"""
Kata: Book Class

Goal:
- Practice basic class creation and instantiation
- Implement attributes: title, author, pages
- Add method: description() → returns summary string
    Title: {title}, Author: {author}, Pages: {pages}

Constraints:
- No external libraries
- Follow TDD: write failing tests first, then implement
"""

from leve_1.code.book import Book


def test_book_class():
    book = Book("1984", "George Orwell", 328)
    assert isinstance(book, Book)
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.pages == 328


def test_book_description():
    book = Book("1984", "George Orwell", 328)
    expected_description = "Title: 1984, Author: George Orwell, Pages: 328"
    assert book.description() == expected_description
