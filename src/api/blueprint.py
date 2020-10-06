from flask import Blueprint
from flask_restx import Api, Namespace

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
rest_api = Api(blueprint)

auth_namespace = Namespace('', 'Authorization')
rest_api.add_namespace(auth_namespace)
user_namespace = Namespace('', 'User operations')
rest_api.add_namespace(user_namespace)
todo_namespace = Namespace('', 'Todo operations')
rest_api.add_namespace(todo_namespace)
