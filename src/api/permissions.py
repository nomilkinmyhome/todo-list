from functools import wraps

from werkzeug.exceptions import Forbidden
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from src.models.user import User
from src.models.todo import Todo


def is_admin(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = User.query.get_or_404(user_id)
        if not user.is_admin:
            raise Forbidden
        return method(*args, **kwargs)
    return wrapper


def is_creator_or_admin(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = User.query.get_or_404(user_id)
        todo = Todo.query.get_or_404(kwargs['pk'])
        if todo.creator_id != user_id and not user.is_admin:
            raise Forbidden
        return method(*args, **kwargs)
    return wrapper


def is_user_or_admin(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = User.query.get_or_404(user_id)
        if user_id != kwargs['pk'] and not user.is_admin:
            raise Forbidden
        return method(*args, **kwargs)
    return wrapper
