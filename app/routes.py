
from os import abort
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
#     Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ]

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET","POST"])
def handle_books():
    if request.method == "GET":							
        books = Book.query.all()						
        books_response = []						
        for book in books:						
            books_response.append({					
                "id": book.id,				
                "title": book.title,				
                "description": book.description				
            })					
        return jsonify(books_response)						

    elif request.method == "POST":			
        request_body = request.get_json()
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])

        db.session.add(new_book)
        db.session.commit()

        return make_response(f"Book {new_book.title} successfully created", 201)



@books_bp.route("/<book_id>", methods=["GET"])	
def handle_planet(book_id):
    book = validate_book(book_id)
   
    return {
        "id": book.id,					
        "title": book.title,					
        "description": book.description,
    }



def validate_book(book_id):
   try:
       book_id = int(book_id)
   except:
       abort(make_response({"message":f"book {book_id} invalid"}, 400))
   
   book = Book.query.get(book_id)
     
   if not book:
      abort(make_response({"message":f"book {book_id} not found"}, 404))
                
   return book

			   
