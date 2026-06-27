from flask import Blueprint

from app.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/register", methods=['POST'])
def register():
    return AuthService.register()

@auth_bp.route("/login", methods=['GET'])
def login():
    return AuthService.login()