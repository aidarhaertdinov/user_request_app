import requests
from tests.user.service import user_login, pytest_user
import pytest


# def test_create_user(delete_user):
#     user = pytest_user()
#     response_create_user = requests.post('http://127.0.0.1:5000/rest/v1/create_user',
#                                          json=user,
#                                          headers={'Authorization': user_login()})
#
#     delete_user(response_create_user.json().get('id'))
#
#     assert 201 == response_create_user.status_code
#     assert 'pytest_user@mail.ru' == response_create_user.json().get('email')

@pytest.mark.parametrize(
    "data, result",
    [
        ({'email': 'pytest_user@mail.ru',
          'password': 'pytest123',
          'permission': 'USER',
          'username': 'Pytest_user'
          }, 201),
        ({'password': 'pytest123',
          'permission': 'USER',
          'username': 'Pytest_user'
          }, 400)
    ]
)
def test_create_user(data, result, delete_user):
    user = data
    response_create_user = requests.post('http://127.0.0.1:5000/rest/v1/create_user',
                                         json=user,
                                         headers={'Authorization': user_login()})

    if response_create_user:
        delete_user(response_create_user.json().get('id'))

    assert result == response_create_user.status_code
    # assert 'pytest_user@mail.ru' == response_create_user.json().get('email')
