from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

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
        
        if len(username) > 100:
            return jsonify({
                "success": False,
                "message": "Username must be within 100 characters"
            }), 400
        
        if len(email) > 255:
            return jsonify({
                "success": False,
                "message": "Email must be within 255 characters"
            }), 400
        
        if len(password) > 255:
            return jsonify({
                "success": False,
                "message": "Password must be within 255 characters"
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

    @staticmethod
    def login():
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({
                "success": False,
                "message": "Email and password are requried"
            }), 400
        
        user = User.query.filter_by(email=email).first()

        if not user:
            return jsonify({
                "success": False,
                "message": "Invalid credentials"
            }), 401
        
        if not check_password_hash(user.password_hash, password):
            return jsonify({
                "success": False,
                "message": "Invalid credentials"
            }), 401
        
        access_token = create_access_token(identity=str(user.id))

        return jsonify({
            "success": True,
            "message": "Login successful",
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }), 200