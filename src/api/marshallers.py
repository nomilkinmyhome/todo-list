from flask_restx import fields

from .blueprint import rest_api

users_list_fields = rest_api.model('UsersList', {
    'id': fields.Integer(),
    'email': fields.String(required=True),
    'is_activated': fields.Boolean(),
    'is_admin': fields.Boolean()
})


tokens_fields = rest_api.model('Tokens', {
    'access_token': fields.String(required=True),
    'refresh_token': fields.String(required=True),
    'csrf_token': fields.String(required=True)
})
