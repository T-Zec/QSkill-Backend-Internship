from flask import Flask

from app.config import Config
from app.extension import db, migrate

from app.routes.book_routes import book_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprint registration
    app.register_blueprint(book_bp)

    # Required model for migration
    from app.models import Book

    return app