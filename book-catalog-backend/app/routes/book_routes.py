from flask import Blueprint

from app.services.book_service import BookService

book_bp = Blueprint('books', __name__, url_prefix="/api/books/")

@book_bp.route("", methods=['POST'])
def create_book():
    return BookService.create_book()

@book_bp.route("", methods=['GET'])
def get_all_books():
    return BookService.get_all_books()

@book_bp.route("/<int:book_id>", methods=['GET'])
def get_book(book_id):
    return BookService.get_book(book_id)

@book_bp.route("<int:book_id>", methods=['PATCH', 'PUT'])
def update_book(book_id):
    return BookService.update_book(book_id)