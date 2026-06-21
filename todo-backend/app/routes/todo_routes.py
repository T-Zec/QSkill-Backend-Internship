from flask import Blueprint
from app.services.todo_service import TodoService

todo_bp = Blueprint('todos', __name__, url_prefix="/api/todos")

@todo_bp.route("", methods=['POST'])
def create_todo():
    return TodoService.create_todo()

@todo_bp.route("", methods=['GET'])
def get_all_todos():
    return TodoService.get_all_todos()

@todo_bp.route("/<int:todo_id>", methods=['GET'])
def get_todo(todo_id):
    return TodoService.get_todo(todo_id)

@todo_bp.route("/<int:todo_id>", methods=['PUT', 'PATCH'])
def update_todo(todo_id):
    return TodoService.update_todo(todo_id)

@todo_bp.route("<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    return TodoService.delete_todo(todo_id)