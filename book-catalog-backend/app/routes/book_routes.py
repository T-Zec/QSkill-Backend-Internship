from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.services.book_service import BookService
from app.decorators import admin_required

book_bp = Blueprint('books', __name__, url_prefix="/api/books/")

# Protected routes for book management
@book_bp.route("", methods=['POST'])
@admin_required
def create_book():
    return BookService.create_book()

@book_bp.route("/<int:book_id>", methods=['PATCH', 'PUT'])
@admin_required
def update_book(book_id):
    return BookService.update_book(book_id)

@book_bp.route("/<int:book_id>", methods=['DELETE'])
@admin_required
def delete_book(book_id):
    return BookService.delete_book(book_id)

@book_bp.route("/clear", methods=['DELETE'])
@admin_required
def clear_books():
    return BookService.clear_books()

# Public routes for book retrieval
@book_bp.route("", methods=['GET'])
@jwt_required()
def get_all_books():
    return BookService.get_all_books()

@book_bp.route("/<int:book_id>", methods=['GET'])
@jwt_required()
def get_book(book_id):
    return BookService.get_book(book_id)

@book_bp.route("/search", methods=['GET'])
@jwt_required()
def search_books():
    return BookService.search_books()

@book_bp.route("/stats", methods=['GET'])
@jwt_required()
def get_book_stats():
    return BookService.get_book_stats()