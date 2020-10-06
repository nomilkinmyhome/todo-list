from app import create_app
from src.models import db
from src.models.user import User


def deploy():
    app = create_app()
    db.create_all(app=app)

    with app.app_context():
        if not db.session.query(User.id).count():
            new_admin = User(email='admin@email.com', is_admin=True, is_activated=True)
            new_admin.set_password('1')
            new_user = User(email='user@email.com', is_activated=True)
            new_user.set_password('2')
            new_non_activated_user = User(email='blocked@email.com')
            new_non_activated_user.set_password('3')

            db.session.add_all((new_admin, new_user, new_non_activated_user))
            db.session.commit()


if __name__ == '__main__':
    deploy()
