from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db, init_db
from models.user import User
import api


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('CONFIG_FILE', silent=True)

    init_db(app)

    app.register_blueprint(api.blueprint)

    return app


app = create_app()


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
