import requests


def user_login() -> str:
    user = {'email': 'admin@mail.ru',
            'password': 'admin123'
            }
    data = requests.post('http://127.0.0.1:5000/auth/login', json=user).json()
    token = f"Bearer {data['token']}"

    return token
