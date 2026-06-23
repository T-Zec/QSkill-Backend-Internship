from flask import request, jsonify
from werkzeug.security import generate_password_hash

from app.extension import db
from app.models import User

class AuthService:
    
    # User authentication
    @staticmethod
    def register():
        data = request.get_json()

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return jsonify({
                "success": False,
                "message": "All fields are required"
            }), 400
        
        existing_user = User.query.filter(
            (User.email == email) | (User.username == username)
        ).first()

        if existing_user:
            return jsonify({
                "success": False,
                "message": "User already exists"
            }), 400
        
        password_hash = generate_password_hash(password)

        user = User(username=username, email=email, password_hash=password_hash)

        db.session.add(user)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "User registered successfully"
        }), 201