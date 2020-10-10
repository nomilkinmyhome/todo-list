from flask_restx import fields

from .blueprint import rest_api

todo_detail_fields = rest_api.model('TodoDetail', {
    'id': fields.Integer(),
    'title': fields.String(),
    'description': fields.String(),
    'is_done': fields.Boolean()
})

user_detail_fields = rest_api.model('UserDetail', {
    'id': fields.Integer(),
    'email': fields.String(),
    'todos': fields.Nested(todo_detail_fields),
    'is_activated': fields.Boolean(),
    'is_admin': fields.Boolean()
})

tokens_fields = rest_api.model('Tokens', {
    'access_token': fields.String(),
    'refresh_token': fields.String()
})
