from flask import request, jsonify

from app.extension import db
from app.models.todo import Todo

class TodoService:

    @staticmethod
    def create_todo():
        data = request.get_json()

        title = data.get("title")
        description = data.get("description")

        if not title:
            return jsonify({
                "success": False,
                "message": "Title is required"
            }), 400

        todo = Todo(title=title, description=description)

        db.session.add(todo)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Todo created successfully",
            "data": todo.to_dict()
        }), 201

    @staticmethod
    def get_all_todos():
        pass

    @staticmethod
    def get_todo(todo_id):
        pass

    @staticmethod
    def update_todo(todo_id):
        pass

    @staticmethod
    def delete_todo(todo_id):
        pass

    @staticmethod
    def complete_todo(todo_id):
        pass