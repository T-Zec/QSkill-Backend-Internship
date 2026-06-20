from datetime import datetime
from app.extension import db

class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String[255], nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }