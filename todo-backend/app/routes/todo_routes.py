from flask import Blueprint
from app.services.todo_service import TodoService

todo_bp = Blueprint('todos', __name__, url_prefix="/api/todos")

@todo_bp.route("", methods=['POST'])
def create_todo():
    return TodoService.create_todo()