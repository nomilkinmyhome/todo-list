from flask_restx import reqparse

auth_parser = reqparse.RequestParser()
auth_parser.add_argument(
    'email',
    type=str,
    required=True,
    location='json'
)
auth_parser.add_argument(
    'password',
    type=str,
    required=True,
    location='json'
)

todo_create_parser = reqparse.RequestParser()
todo_create_parser.add_argument(
    'title',
    type=str,
    required=True,
    location='json'
)
todo_create_parser.add_argument(
    'description',
    type=str,
    required=True,
    location='json'
)

todo_update_parser = reqparse.RequestParser()
todo_update_parser.add_argument(
    'title',
    type=str,
    required=False,
    location='json'
)
todo_update_parser.add_argument(
    'description',
    type=str,
    required=False,
    location='json'
)
todo_update_parser.add_argument(
    'is_done',
    type=bool,
    required=False,
    location='json'
)
