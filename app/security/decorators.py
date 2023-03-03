from flask import current_app
from json.decoder import JSONDecodeError


def auto_login(func):
    def wrapper(*args, **kwargs):
        from app import user_repository
        try:
            return func(*args, **kwargs)

        except JSONDecodeError:
            user_repository.user_login(
                {
                    'email': current_app.config.get('ADMIN_EMAIL'),
                    'password': current_app.config.get('ADMIN_PASSWORD')
                }
            )
            return func(*args, **kwargs)

    return wrapper
