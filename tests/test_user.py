import requests
from service import user_login


def test_create_user():
    user = {'email': 'pytest_user@mail.ru',
            'password': 'pytest123',
            'permission': 'USER',
            'username': 'Pytest_user'
            }
    response_create_user = requests.post('http://127.0.0.1:5000/rest/v1/create_user',
                                         json=user,
                                         headers={'Authorization': user_login()})

    assert 201 == response_create_user.status_code

    response_delete = requests.delete(f"http://127.0.0.1:5000/rest/v1/users/{response_create_user.json().get('id')}",
                                      headers={'Authorization': user_login()})

    assert 200 == response_delete.status_code


def test_update_user():

    user = {'email': 'pytest_user@mail.ru',
            'password': 'pytest123',
            'permission': 'USER',
            'username': 'Py'
            }
    response_create_user = requests.post('http://127.0.0.1:5000/rest/v1/create_user',
                             json=user,
                             headers={'Authorization': user_login()})

    assert 201 == response_create_user.status_code

    update_user = {'email': 'pytest_user@mail.ru',
                   'password': 'pytest123',
                   'permission': 'USER',
                   'username': 'Pytest_user'
                   }
    response_update = requests.put(f"http://127.0.0.1:5000/rest/v1/users/{response_create_user.json().get('id')}",
                                   json=update_user,
                                   headers={'Authorization': user_login()})

    assert 200 == response_update.status_code

    response_delete = requests.delete(f"http://127.0.0.1:5000/rest/v1/users/{response_create_user.json().get('id')}",
                                      headers={'Authorization': user_login()})

    assert 200 == response_delete.status_code
