import requests
from service import user_login


def test_create_user():
    user = {'email': 'user5@mail.ru',
            'password': 'user5',
            'permission': 'USER',
            'username': 'Кtytr'
            }
    response = requests.post('http://127.0.0.1:5000/rest/v1/create_user',
                             json=user,
                             headers={'Authorization': user_login()})

    assert 201 == response.status_code


def test_update_user():

    user = {'email': 'user10@mail.ru',
            'password': 'user10',
            'permission': 'USER',
            'username': 'В'
            }
    response = requests.post('http://127.0.0.1:5000/rest/v1/create_user',
                             json=user,
                             headers={'Authorization': user_login()})
    assert 201 == response.status_code

    update_user = {'email': 'user10@mail.ru',
                   'password': 'user10',
                   'permission': 'USER',
                   'username': 'Виталий'
                   }
    response_update = requests.put('http://127.0.0.1:5000/rest/v1/users/14',
                                   json=update_user,
                                   headers={'Authorization': user_login()})

    assert 200 == response_update.status_code
