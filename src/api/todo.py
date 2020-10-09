from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource
from werkzeug.exceptions import Forbidden

from use_cases.todo import create_todo, update_todo, delete_todo, get_todo_info
from .blueprint import rest_api, todo_namespace
from .marshallers import todo_detail_fields
from .permissions import is_admin, is_creator


@todo_namespace.route('/todo/create')
class TodoCreate(Resource):
    @jwt_required
    @todo_namespace.marshal_with(todo_detail_fields)
    def post(self):
        user_id = get_jwt_identity()
        return create_todo(user_id, rest_api.payload)


@todo_namespace.route('/todo/<int:pk>')
class TodoDetail(Resource):
    @jwt_required
    @todo_namespace.marshal_with(todo_detail_fields)
    def get(self, pk):
        user_id = get_jwt_identity()
        if not is_admin(user_id) and not is_creator(user_id, pk):
            raise Forbidden
        return get_todo_info(pk)

    @jwt_required
    @todo_namespace.marshal_with(todo_detail_fields)
    def put(self, pk):
        user_id = get_jwt_identity()
        if not is_admin(user_id) and not is_creator(user_id, pk):
            raise Forbidden
        return update_todo(pk, rest_api.payload)

    @jwt_required
    def delete(self, pk):
        user_id = get_jwt_identity()
        if not is_admin(user_id) and not is_creator(user_id, pk):
            raise Forbidden
        delete_todo(pk)
        return {'status': 'ok'}
