from models.user import User


def is_admin(user_id):
    user = User.query.get(user_id)
    return bool(user and user.is_admin)
