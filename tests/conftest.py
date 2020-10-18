import pytest

from src.app import create_app
from src.models import db
from src.models.user import User
from src.models.todo import Todo  # noqa: F401


@pytest.fixture(scope='session')
def client():
    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()

            yield client


@pytest.fixture
def user():
    user = User(email='user@email.com', is_activated=True)
    user.set_password('1')
    db.session.add(user)
    db.session.commit()

    yield user
