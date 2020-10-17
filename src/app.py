import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager

from src.models import db, init_db
from src.models.user import User
from src.models.todo import Todo  # noqa: F401
import src.api
import src.pages


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('CONFIG_FILE', silent=True)

    if not app.config['SECRET_KEY']:
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    if not app.config['SQLALCHEMY_DATABASE_URI']:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    init_db(app)

    app.register_blueprint(src.api.blueprint)
    app.register_blueprint(src.pages.blueprint)

    return app


app = create_app()
jwt = JWTManager(app)


def init_manager(app, db):
    Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    return manager


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


manager = init_manager(app, db)


if __name__ == '__main__':
    app.run()
