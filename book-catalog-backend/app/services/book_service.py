from flask import request, jsonify

from app.extension import db
from app.models.book import Book

class BookService:

    # CRUD operations
    @staticmethod
    def create_book():
        data = request.get_json()

        title = data.get("title")
        author = data.get("author")
        
        if not title:
            return jsonify({
                "success": False,
                "message": "Book title is required"
            }), 400

        if len(title) > 255:
            return jsonify({
                "success": False,
                "message": "Book title cannot not exceed 255 characters"
            }), 400
        
        if not author:
            return jsonify({
                "success": "Author name is required"
            }), 400
        
        if len(author) > 255:
            return jsonify({
                "success": False,
                "message": "Author name cannot exceed 255 characters"
            }), 400
        
        book = Book(
            title=data["title"],
            author=data["author"],
            genre=data["genre"],
            publication_year=data["publication_year"],
            availability=data["availability"]
        )

        db.session.add(book)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Book created successfully",
            "data": book.to_dict()
        }), 201
    
    @staticmethod
    def get_all_books():
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)
        availability = request.args.get('availability')
        title = request.args.get('title', type=str)
        author = request.args.get('author', type=str)

        if per_page > 100:
            per_page = 100

        query = Book.query

        if availability is not None:
            is_available = availability.lower() == 'true'
            query = query.filter(Book.availability == is_available)

        if title:
            query = query.filter(Book.title.ilike(f"%{title}%"))

        if author:
            query = query.filter(Book.author.ilike(f"%{author}%"))

        pagination = query.order_by(Book.created_at.desc()).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        books = pagination.items

        return jsonify({
            "success": True,
            "pagination": {
                "page": pagination.page,
                "per_page": pagination.per_page,
                "total_pages": pagination.pages,
                "total_items": pagination.total,
                "has_next": pagination.has_next,
                "has_prev": pagination.has_prev
            },
            "data": [book.to_dict() for book in books]
        }), 200