from flask_login import UserMixin
from enum import Enum

class Permissions(Enum):
    MODERATE = "MODERATE"
    ADMIN = "ADMIN"
    USER = "USER"

class User(UserMixin):

    def __init__(self, id, username, email, permission):
        self.id = id
        self.username = username
        self.email = email
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
        return User(id=_dict.get('id'),
                    username=_dict.get('username'),
                    email=_dict.get('email'),
                    permission=_dict.get('permission'))



