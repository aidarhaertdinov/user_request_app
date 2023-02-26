# from app import user_repository
from flask import current_app, abort
from functools import wraps
from config import Config


def auto_login(function, *args, **kwargs):
    @wraps(function)
    def wrapp(*args, **kwargs):
        result = function(*args, **kwargs)
        if abort(400):
            user_repository.user_login(user)
            return function(*args, **kwargs)
        elif abort(400):
            user_repository.user_login(user)
            return function(*args, **kwargs)
        else:
            abort(400)

    return wrapp


def decorator_function(func):
    def wrapper(*args, **kwargs):
        from app import user_repository
        try:
            func(*args, **kwargs)
        except Exception:
            user_repository.user_login(
                {
                    'email': Config.ADMIN_EMAIL,
                    'password': Config.ADMIN_PASSWORD
                }
            )
            return func(*args, **kwargs)

    return wrapper
