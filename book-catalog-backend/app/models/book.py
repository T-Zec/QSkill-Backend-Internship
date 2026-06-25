from app.extension import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String[255], unique=True, nullable=False)
    author = db.Column(db.String[255], nullable=False)
    genre = db.Column(db.String[100])
    publication_year = db.Column(db.Integer[4])
    availability = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "publication_year": self.publication_year,
            "availability": self.availability,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }