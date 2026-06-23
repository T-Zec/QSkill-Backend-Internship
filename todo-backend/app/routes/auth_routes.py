from flask import Blueprint
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/me', methods=['GET'])
def me():
    return {
        "message": "Protected route works"
    }

@auth_bp.route("/register", methods=['POST'])
def register():
    return AuthService.register()