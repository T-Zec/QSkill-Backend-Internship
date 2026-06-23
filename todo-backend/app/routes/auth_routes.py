from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route("/register", methods=['POST'])
def register():
    return AuthService.register()

@auth_bp.route("/login", methods=['POST'])
def login():
    return AuthService.login()

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    current_user = get_jwt_identity()

    return {
        "success": True,
        "user_id": current_user
    }, 200