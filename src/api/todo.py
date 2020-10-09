from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource

from use_cases.todo import create_todo, update_todo, delete_todo, get_todo_info
from .blueprint import rest_api, todo_namespace
from .marshallers import todo_detail_fields
from .permissions import is_creator_or_admin


@todo_namespace.route('/todo/create')
class TodoCreate(Resource):
    @jwt_required
    @todo_namespace.marshal_with(todo_detail_fields)
    def post(self):
        user_id = get_jwt_identity()
        return create_todo(user_id, rest_api.payload)


@todo_namespace.route('/todo/<int:pk>')
class TodoDetail(Resource):
    @todo_namespace.marshal_with(todo_detail_fields)
    @is_creator_or_admin
    def get(self, pk):
        return get_todo_info(pk)

    @todo_namespace.marshal_with(todo_detail_fields)
    @is_creator_or_admin
    def put(self, pk):
        return update_todo(pk, rest_api.payload)

    @is_creator_or_admin
    def delete(self, pk):
        delete_todo(pk)
        return {'status': 'ok'}
