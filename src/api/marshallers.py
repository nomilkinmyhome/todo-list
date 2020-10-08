from flask_restx import fields

from .blueprint import rest_api

user_detail_fields = rest_api.model('UserDetail', {
    'id': fields.Integer(),
    'email': fields.String(),
    'is_activated': fields.Boolean(),
    'is_admin': fields.Boolean()
})


tokens_fields = rest_api.model('Tokens', {
    'access_token': fields.String(),
    'refresh_token': fields.String(),
    'csrf_token': fields.String()
})
