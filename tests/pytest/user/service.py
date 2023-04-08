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


def request_get(id):
    return requests.get(f'http://127.0.0.1:5000/rest/v1/users/{id}',
                        headers={'Authorization': user_login()})


def create_user_request(user):
    return requests.post('http://127.0.0.1:5000/rest/v1/create_user',
                         json=user,
                         headers={'Authorization': user_login()})


def request_put(update_user, id):
    return requests.put(f"http://127.0.0.1:5000/rest/v1/users/{id}",
                        json=update_user,
                        headers={'Authorization': user_login()})


def request_delete(id):
    return requests.delete(f"http://127.0.0.1:5000/rest/v1/users/{id}",
                           headers={'Authorization': user_login()})
