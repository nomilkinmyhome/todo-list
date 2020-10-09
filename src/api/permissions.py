from models.user import User
from models.todo import Todo


def is_admin(user_id):
    user = User.query.get(user_id)
    return bool(user and user.is_admin)


def is_creator(user_id, todo_id):
    todo = Todo.query.get(todo_id)
    return todo.creator_id == user_id
