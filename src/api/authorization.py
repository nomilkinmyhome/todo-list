from flask_restx import Resource
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity

from use_cases.authorization import auth, refresh
from .blueprint import auth_namespace, rest_api
from .marshallers import tokens_fields


@auth_namespace.route('/auth/login')
class Auth(Resource):
    @auth_namespace.marshal_with(tokens_fields)
    def post(self):
        email, password = rest_api.payload['email'], rest_api.payload['password']
        return auth(email, password)


@auth_namespace.route('/auth/refresh')
class Refresh(Resource):
    @jwt_refresh_token_required
    @auth_namespace.marshal_with(tokens_fields)
    def post(self):
        user_id = get_jwt_identity()
        return refresh(user_id)
