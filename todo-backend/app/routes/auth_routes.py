from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route("/register", methods=['POST'])
def register():
    return AuthService.register()

@auth_bp.route("/login", methods=['POST'])
def login():
    return AuthService.login()

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    return AuthService.profile()