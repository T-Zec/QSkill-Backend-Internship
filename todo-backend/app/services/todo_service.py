from flask import request, jsonify

from app.extension import db
from app.models.todo import Todo

class TodoService:

    # CRUD operation
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
        todos = Todo.query.all()

        return jsonify({
            "success": True,
            "count": len(todos),
            "data": [todo.to_dict() for todo in todos]
        }), 200

    @staticmethod
    def get_todo(todo_id):
        # todo = Todo.query.get(todo_id)
        todo = db.session.get(Todo, todo_id)

        if not todo:
            return jsonify({
                "success": False,
                "message": "Todo not found"
            }), 404
        
        return jsonify({
            "success": True,
            "data": todo.to_dict()
        }), 200

    @staticmethod
    def update_todo(todo_id):
        todo = db.session.get(Todo, todo_id)

        if not todo:
            return jsonify({
                "success": False,
                "message": "Todo not found"
            }), 404        

        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "No data provided"
            }), 400        
        
        for key, value in data.items():
            if hasattr(todo, key):
                setattr(todo, key, value)

        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Todo updated successfully",
            "data": todo.to_dict()
        }), 200

    @staticmethod
    def delete_todo(todo_id):
        todo = db.session.get(Todo, todo_id)

        if not todo:
            return ({
                "success": False,
                "message": "Todo not found"
            }), 404

        db.session.delete(todo)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Todo deleted successfully"
        }), 200

    # Mark/unmark todo tasks as read
    @staticmethod
    def complete_todo(todo_id):
        todo = db.session.get(Todo, todo_id)

        if not todo:
            return jsonify({
                "success": False,
                "message": "Todo not found"
            }), 404
        
        if todo.is_completed == True:
            return jsonify({
                "success": False,
                "message": "Todo already marked as completed"
            }), 400
        
        todo.is_completed = True
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Todo marked as completed",
            "data": todo.to_dict()
        }), 200
    
    @staticmethod
    def imcomplete_todo(todo_id):
        todo = db.session.get(Todo, todo_id)

        if not todo:
            return jsonify({
                "success": False,
                "message": "Todo not found"
            }), 404

        if todo.is_completed == False:
            return jsonify({
                "success": False,
                "message": "Todo already unmarked as incompleted"
            }), 400
        
        todo.is_completed = False
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Todo unmarked as incompleted",
            "data": todo.to_dict()
        }), 200