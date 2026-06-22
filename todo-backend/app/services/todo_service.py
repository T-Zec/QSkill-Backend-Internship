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
        
        if len(title) > 255:
            return jsonify({
                "success": False,
                "message": "Title cannot exceed 255 characters"
            }), 400 

        if not title.strip():
            return jsonify({
                "success": False,
                "message": "Title is required"
            }), 400

        todo = Todo(title=title.strip(), description=description)

        db.session.add(todo)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Todo created successfully",
            "data": todo.to_dict()
        }), 201

    @staticmethod
    def get_all_todos():
        # todos = Todo.query.all()
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        completed = request.args.get('completed')

        if per_page > 100:
            per_page = 100

        query = Todo.query

        if completed is not None:
            is_completed = completed.lower() == "true"
            query = query.filter(Todo.is_completed == is_completed)

        pagination = query.order_by(Todo.created_at.desc()).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        todos = pagination.items

        # return jsonify({
        #     "success": True,
        #     "count": len(todos),
        #     "data": [todo.to_dict() for todo in todos]
        # }), 200

        return jsonify({
            "success": True,
            "pagination": {
                "page": pagination.page,
                "per_page": pagination.per_page,
                "total": pagination.total,
                "pages": pagination.pages,
                "has_next": pagination.has_next,
                "has_prev": pagination.has_prev
            },
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
            return jsonify({
                "success": False,
                "message": "Todo not found"
            }), 404

        db.session.delete(todo)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Todo deleted successfully"
        }), 200
    
    @staticmethod
    def clear_todos():
        if not Todo.query.first():
            return jsonify({
                "success": False,
                "message": "No todos to clear"
            }), 400
        
        Todo.query.delete()
        db.session.commit()
        return jsonify({
            "success": True,
            "message": "All todos cleared successfully"
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
    def incomplete_todo(todo_id):
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