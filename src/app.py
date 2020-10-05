from flask import Flask

import api


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('CONFIG_FILE', silent=True)

    app.register_blueprint(api.blueprint)

    return app


app = create_app()


if __name__ == '__main__':
    app.run()
