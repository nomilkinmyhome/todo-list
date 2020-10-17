from src.use_cases.todo import create_todo, update_todo


def test_create_todo(client, user):
    payload = {
        'title': 'test todo',
        'description': 'very long and useful description',
    }
    todo = create_todo(user.id, payload)

    assert todo.id == 1
    assert todo.title == payload['title']


def test_update_todo(client):
    todo_id = 1
    old_description = 'very long and useful description'
    payload = {'title': 'new title'}
    todo = update_todo(todo_id, payload)

    assert todo.title == payload['title']
    assert todo.description == old_description
