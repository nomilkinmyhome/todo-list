from models import db
from models.todo import Todo


def get_todo_info(todo_id):
    return Todo.query.get_or_404(todo_id)


def create_todo(user_id, payload):
    todo = Todo(**payload, creator_id=user_id)
    db.session.add(todo)
    db.session.commit()
    return todo


def update_todo(todo_id, payload):
    todo = Todo.query.get_or_404(todo_id)
    for key, value in payload.items():
        setattr(todo, key, value)
    db.session.add(todo)
    db.session.commit()
    return todo


def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
