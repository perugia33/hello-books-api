
from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Sketches in Spain Part 1", "An Art Journal and guide."),
    Book(2, "Sketches in Spain Part 2", "An Art Journal and guide."),
    Book(3, "Sketches in Spain Part 1", "An Art Journal and guide.")
]

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

# GETTING ALL BOOKS
@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return jsonify(books_response)

# Getting One Book with its description
@books_bp.route("/<book_id>", methods=["GET"])	


def handle_book(book_id):			
    book_id = int(book_id) 
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id, 
                "title": book.title,
                 "description": book.description }
            					