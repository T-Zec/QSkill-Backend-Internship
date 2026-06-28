from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

from app.extension import db
from app.models.book import Book

class BookService:

    # CRUD operations
    @staticmethod
    def create_book():
        data = request.get_json()

        title = data.get("title")
        author = data.get("author")
        year = data.get("publication_year")
        
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
                "success": False,
                "message": "Author name is required"
            }), 400
        
        if Book.query.filter_by(title=title).first():
            return jsonify({
                "success": False,
                "message": "Book with this title already exists"
            }), 400
        
        if len(author) > 255:
            return jsonify({
                "success": False,
                "message": "Author name cannot exceed 255 characters"
            }), 400
        
        if len(str(year)) != 4:
            return jsonify({
                "success": False,
                "message": "The publication year must be of 4 digits"
            }), 400
        
        current_user_id = int(get_jwt_identity())
        
        book = Book(
            title=data["title"].strip(),
            author=data["author"].strip(),
            genre=data["genre"].strip(),
            publication_year=data["publication_year"],
            availability=data["availability"],
            user_id=current_user_id
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
        title = request.args.get('title', type=str)
        author = request.args.get('author', type=str)
        genre = request.args.get("genre", type=str)
        year = request.args.get("year", type=int)
        availability = request.args.get('availability')

        if per_page > 100:
            per_page = 100

        query = Book.query

        if availability is not None:
            is_available = True if availability.lower() == 'true' else False if availability.lower() == 'false' else availability
            query = query.filter(Book.availability == is_available)

        if title:
            query = query.filter(Book.title.ilike(f"%{title}%"))

        if author:
            query = query.filter(Book.author.ilike(f"%{author}%"))

        if genre:
            query = query.filter(Book.genre.ilike(f"%{genre}%"))

        if year and len(str(year)) == 4:
            query = query.filter(Book.publication_year.ilike(f"{year}"))

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

    @staticmethod
    def get_book(book_id):
        book = Book.query.get(book_id)

        if not book:
            return jsonify({
                "success": False,
                "message": "Book not found"
            }), 404
        
        return jsonify({
            "success": True,
            "data": book.to_dict()
        }), 200
    
    @staticmethod
    def update_book(book_id):
        current_user_id = int(get_jwt_identity())
        
        book = Book.query.filter_by(id=book_id, user_id=current_user_id).first()

        if not book:
            return jsonify({
                "success": False,
                "message": "Book not found"
            }), 404

        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "No data provided"
            }), 400
        
        for key, value in data.items():
            if hasattr(book, key):
                setattr(book, key, value)

        db.session.commit()

        return jsonify({
            "success": True,
            "message": "book updated successfully",
            "data": book.to_dict()
        }), 200
    
    @staticmethod
    def delete_book(book_id):
        current_user_id = int(get_jwt_identity())

        book = Book.query.filter_by(id=book_id, user_id=current_user_id).first()

        if not book:
            return jsonify({
                "success": False,
                "message": "Book not found"
            }), 404

        db.session.delete(book)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Book deleted successfully"
        }), 200
    
    @staticmethod
    def clear_books():
        current_user_id = int(get_jwt_identity())

        if not Book.query.filter_by(user_id=current_user_id).first():
            return jsonify({
                "success": False,
                "message": "No books to clear"
            }), 404

        Book.query.filter_by(user_id=current_user_id).delete()
        db.session.commit()        

        return jsonify({
            "success": True,
            "message": "All books cleared successfully"
        }), 200
    
    @staticmethod
    def search_books():
        title = request.args.get('title', type=str)
        author = request.args.get('author', type=str)
        genre = request.args.get("genre", type=str)
        year = request.args.get("year", type=int)
        availability = request.args.get('availability')

        query = Book.query

        if availability is not None:
            is_available = True if availability.lower() == 'true' else False if availability.lower() == 'false' else availability
            query = query.filter(Book.availability == is_available)

        if title:
            query = query.filter(Book.title.ilike(f"%{title}%"))

        if author:
            query = query.filter(Book.author.ilike(f"%{author}%"))

        if genre:
            query = query.filter(Book.genre.ilike(f"%{genre}%"))

        if year and len(str(year)) == 4:
            query = query.filter(Book.publication_year.ilike(f"{year}"))

        books = query.all()

        return jsonify({
            "success": True,
            "data": [book.to_dict() for book in books]
        }), 200
    
    @staticmethod
    def get_book_stats():
        total_books = Book.query.count()
        available_books = Book.query.filter_by(availability=True).count()
        unavailable_books = Book.query.filter_by(availability=False).count()

        return jsonify({
            "success": True,
            "data": {
                "total_books": total_books,
                "available_books": available_books,
                "unavailable_books": unavailable_books
            }
        }), 200