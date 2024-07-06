import pytest
from app.models.book import Book

def test_book_to_dict():
    # Arrange
    book = Book(id=1, title="Test Book", description="Test Description")

    # Act
    book_dict = book.to_dict()

    # Assert
    assert book_dict == {
        'id': 1,
        'title': 'Test Book',
        'description': 'Test Description'
    }


def test_book_from_dict():
    # Arrange
    book_dict = {
        'title': 'Test Book',
        'description': 'Test Description'
    }

    # Act
    book = Book.from_dict(book_dict)

    # Assert
    assert book.title == 'Test Book'
    assert book.description == 'Test Description'


def test_book_from_dict_missing_description():
    # Arrange
    book_dict = {
        'title': 'Test Book'
    }

    # Assert
    with pytest.raises(ValueError):
        # Act
        Book.from_dict(book_dict)

def test_book_from_dict_missing_title():
    # Arrange
    book_dict = {
        'description': 'Test Description'
    }

    # Assert
    with pytest.raises(ValueError):
        # Act
        Book.from_dict(book_dict)