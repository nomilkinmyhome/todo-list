import re

from flask_login import UserMixin
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash

from src.models import db
from src.exceptions import InvalidEmail


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(128))

    is_admin = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
    is_activated = db.Column(db.Boolean, default=False)

    @validates('email')
    def validate_email(self, key, email):
        if not re.search(r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', email):
            raise InvalidEmail

        return email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User: {self.email}; ID: {self.id}>'
