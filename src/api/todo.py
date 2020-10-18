from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource

from src.use_cases.todo import (
    create_todo,
    update_todo,
    delete_todo,
    get_todo_info
)
from .blueprint import todo_namespace
from .marshallers import todo_detail_fields
from .permissions import is_creator_or_admin
from .parsers import todo_create_parser, todo_update_parser


@todo_namespace.route('/todo/create')
class TodoCreate(Resource):
    @jwt_required
    @todo_namespace.marshal_with(todo_detail_fields)
    @todo_namespace.expect(todo_create_parser)
    def post(self):
        user_id = get_jwt_identity()
        payload = todo_create_parser.parse_args(strict=True)
        return create_todo(user_id, payload)


@todo_namespace.route('/todo/<int:pk>')
class TodoDetail(Resource):
    @todo_namespace.marshal_with(todo_detail_fields)
    @is_creator_or_admin
    def get(self, pk):
        return get_todo_info(pk)

    @todo_namespace.marshal_with(todo_detail_fields)
    @todo_namespace.expect(todo_update_parser)
    @is_creator_or_admin
    def put(self, pk):
        payload = todo_update_parser.parse_args(strict=True)
        return update_todo(pk, payload)

    @is_creator_or_admin
    def delete(self, pk):
        delete_todo(pk)
        return {'status': 'ok'}
