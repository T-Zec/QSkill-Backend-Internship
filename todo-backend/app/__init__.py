from flask import Flask
from app.config import Config
from app.extension import db, migrate, jwt

from app.routes.todo_routes import todo_bp
from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(todo_bp)

    # Requird model for migration
    from app.models import Todo
    from app.models import User

    return app