from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource
from werkzeug.exceptions import Forbidden

from use_cases.user import user_is_admin, get_users_list
from .blueprint import user_namespace
from .marshallers import users_list_fields


@user_namespace.route('/users')
class UsersList(Resource):
    @jwt_required
    @user_namespace.marshal_with(users_list_fields)
    def get(self):
        user_id = get_jwt_identity()
        if not user_is_admin(user_id):
            raise Forbidden
        return get_users_list()
