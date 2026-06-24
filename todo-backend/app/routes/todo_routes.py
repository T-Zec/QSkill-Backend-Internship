from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.services.todo_service import TodoService

todo_bp = Blueprint('todos', __name__, url_prefix="/api/todos")

@todo_bp.route("", methods=['POST'])
@jwt_required()
def create_todo():
    return TodoService.create_todo()

@todo_bp.route("", methods=['GET'])
@jwt_required()
def get_all_todos():
    return TodoService.get_all_todos()

@todo_bp.route("/<int:todo_id>", methods=['GET'])
@jwt_required()
def get_todo(todo_id):
    return TodoService.get_todo(todo_id)

@todo_bp.route("/<int:todo_id>", methods=['PUT', 'PATCH'])
@jwt_required()
def update_todo(todo_id):
    return TodoService.update_todo(todo_id)

@todo_bp.route("/<int:todo_id>", methods=["DELETE"])
@jwt_required()
def delete_todo(todo_id):
    return TodoService.delete_todo(todo_id)

@todo_bp.route("/clear", methods=["DELETE"])
@jwt_required()
def clear_todos():
    return TodoService.clear_todos()


@todo_bp.route("/<int:todo_id>/complete", methods=['PATCH'])
@jwt_required()
def complete_todo(todo_id):
    return TodoService.complete_todo(todo_id)

@todo_bp.route("/<int:todo_id>/incomplete", methods=['PATCH'])
@jwt_required()
def incomplete_todo(todo_id):
    return TodoService.incomplete_todo(todo_id)
