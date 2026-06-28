from flask_jwt_extended import get_jwt, jwt_required
from functools import wraps
from flask import jsonify

def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        claims = get_jwt()

        if claims.get("role") != "admin":
            return jsonify({
                "success": False,
                "message": "Admin access required"
            }), 403
        
        return fn(*args, **kwargs)
    return wrapper