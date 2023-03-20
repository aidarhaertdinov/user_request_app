import requests


def pytest_user():

    return {'email': 'pytest_user@mail.ru',
            'password': 'pytest123',
            'permission': 'USER',
            'username': 'Pytest_user'
            }


def user_login() -> str:
    user = {'email': 'admin@mail.ru',
            'password': 'admin123'
            }
    data = requests.post('http://127.0.0.1:5000/auth/login', json=user).json()
    token = f"Bearer {data['token']}"

    return token
