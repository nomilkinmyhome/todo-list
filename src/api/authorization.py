from flask_restx import Resource
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity

from use_cases.authorization import auth, refresh
from .blueprint import auth_namespace
from .marshallers import tokens_fields
from .parsers import auth_parser


@auth_namespace.route('/auth/login')
class Auth(Resource):
    @auth_namespace.marshal_with(tokens_fields)
    @auth_namespace.expect(auth_parser)
    def post(self):
        args = auth_parser.parse_args(strict=True)
        return auth(args['email'], args['password'])


@auth_namespace.route('/auth/refresh')
class Refresh(Resource):
    @jwt_refresh_token_required
    @auth_namespace.marshal_with(tokens_fields)
    def post(self):
        user_id = get_jwt_identity()
        return refresh(user_id)
