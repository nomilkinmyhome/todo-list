from flask import Blueprint
from flask_restx import Api, Namespace
from flask_jwt_extended.exceptions import (WrongTokenError,
                                           NoAuthorizationError,
                                           JWTDecodeError,
                                           InvalidHeaderError,
                                           RevokedTokenError,
                                           FreshTokenRequired,
                                           UserLoadError)
from werkzeug.exceptions import Forbidden

from src.exceptions import InvalidCredentials, UserIsBlocked

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
rest_api = Api(blueprint)

auth_namespace = Namespace('', 'Authorization')
rest_api.add_namespace(auth_namespace)
user_namespace = Namespace('', 'User operations')
rest_api.add_namespace(user_namespace)
todo_namespace = Namespace('', 'Todo operations')
rest_api.add_namespace(todo_namespace)


@rest_api.errorhandler(FreshTokenRequired)
@rest_api.errorhandler(JWTDecodeError)
@rest_api.errorhandler(InvalidHeaderError)
@rest_api.errorhandler(RevokedTokenError)
@rest_api.errorhandler(UserLoadError)
@rest_api.errorhandler(NoAuthorizationError)
@rest_api.errorhandler(WrongTokenError)
@rest_api.errorhandler(InvalidCredentials)
def handle_invalid_credentials_error(error):
    return {'message': str(error)}, 401


@rest_api.errorhandler(Forbidden)
def handle_forbidden(error):
    return {'message': str(error)}, 403


@rest_api.errorhandler(UserIsBlocked)
def handle_user_is_blocked_error(error):
    return {'message': str(error)}, 403
