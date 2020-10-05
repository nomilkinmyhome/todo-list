from app import create_app
from src.models import db
from src.models.user import User


def deploy():
    app = create_app()
    db.create_all(app=app)

    with app.app_context():
        if not db.session.query(User.id).count():
            new_admin = User(email='admin@email.com', is_admin=True)
            new_admin.set_password('1')

            db.session.add(new_admin)
            db.session.commit()


if __name__ == '__main__':
    deploy()
