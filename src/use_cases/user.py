from models.user import User


def get_users_list(page=1, per_page=5):
    users = User.query.paginate(page=page, per_page=per_page, error_out=False)
    return users.items
