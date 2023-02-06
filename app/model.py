from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum
from datetime import datetime

class Permissions(Enum):
    MODERATE = "MODERATE"
    ADMIN = "ADMIN"
    USER = "USER"

class User():

    def __init__(self, username, email, permission=Permissions.USER):
        self.username = username
        self.email = email
        self.password = password
        self.permission = permission

    def can(self, perm):
        return self.permission is not None and self.permission == perm

    def to_json(self):
        return {'id': self.id,
                'username': self.username,
                'email': self.email,
                'permission': self.permission.value}

    @staticmethod
    def from_json(_dict: dict):
        return User(email=_dict.get('email'),
                    username=_dict.get('username'),
                    password=_dict.get('password'),
                    permission=Permissions.__getitem__(_dict.get('permission')))

