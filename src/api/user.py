from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource
from werkzeug.exceptions import Forbidden

from use_cases.user import get_users_list, get_user_info
from .blueprint import user_namespace
from .marshallers import user_detail_fields
from .permissions import is_admin


@user_namespace.route('/users')
class UsersList(Resource):
    @jwt_required
    @user_namespace.marshal_with(user_detail_fields)
    def get(self):
        user_id = get_jwt_identity()
        if not is_admin(user_id):
            raise Forbidden
        return get_users_list()


@user_namespace.route('/user/<int:pk>')
class UserDetail(Resource):
    @jwt_required
    @user_namespace.marshal_with(user_detail_fields)
    def get(self, pk):
        user_id = get_jwt_identity()
        if not is_admin(user_id) and user_id != pk:
            raise Forbidden
        return get_user_info(pk)
