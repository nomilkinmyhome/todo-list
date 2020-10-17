from flask_restx import Resource

from src.use_cases.user import get_users_list, get_user_info
from .blueprint import user_namespace
from .marshallers import user_detail_fields
from .permissions import is_admin, is_user_or_admin


@user_namespace.route('/users')
class UsersList(Resource):
    @user_namespace.marshal_with(user_detail_fields)
    @is_admin
    def get(self):
        return get_users_list()


@user_namespace.route('/user/<int:pk>')
class UserDetail(Resource):
    @user_namespace.marshal_with(user_detail_fields)
    @is_user_or_admin
    def get(self, pk):
        return get_user_info(pk)
