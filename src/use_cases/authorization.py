from flask_jwt_extended import create_access_token, create_refresh_token
import flask_wtf.csrf

from exceptions import UserIsBlocked, InvalidCredentials
from models.user import User


def get_tokens(user):
    if not user or not user.is_activated:
        raise UserIsBlocked
    return {'access_token': create_access_token(user.id),
            'refresh_token': create_refresh_token(user.id),
            'csrf_token': flask_wtf.csrf.generate_csrf()}


def refresh(user_id):
    user = User.query.filter_by(id=user_id).first()
    return get_tokens(user)


def auth(email, password):
    user = User.query.filter_by(email=email).first_or_404()
    if not user or not user.check_password(password):
        raise InvalidCredentials
    return get_tokens(user)
