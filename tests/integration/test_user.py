import requests
from tests.integration.service import user_login


def test_create_user(delete_user):
    user = {'email': 'pytest_user@mail.ru',
            'password': 'pytest123',
            'permission': 'USER',
            'username': 'Pytest_user'
            }
    response_create_user = requests.post('http://127.0.0.1:5000/rest/v1/create_user',
                                         json=user,
                                         headers={'Authorization': user_login()})

    assert 201 == response_create_user.status_code

    return response_create_user



def test_update_user(create_user_for_update):
    update_user = {'email': 'pytest_user@mail.ru',
                   'password': 'pytest123',
                   'permission': 'USER',
                   'username': 'Pytest_user'
                   }
    response_update = requests.put(f"http://127.0.0.1:5000/rest/v1/users/{create_user_for_update.json().get('id')}",
                                   json=update_user,
                                   headers={'Authorization': user_login()})

    assert 200 == response_update.status_code

