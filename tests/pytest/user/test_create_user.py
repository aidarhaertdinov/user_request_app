import requests

from tests.pytest.user.service import pytest_user, create_user_request, user_login
import pytest


@pytest.mark.parametrize(
    "data, result",
    [
        ({'email': 'pytest_user@mail.ru',
          'password': 'pytest123',
          'permission': 'USER',
          'username': 'Pytest_user'
          }, 201),
        ({'email': 'pytest_user@mail.ru',
          'password': 'pytest123',
          'permission': 'MODERATE',
          'username': 'Pytest_user'
          }, 201),
        ({'email': 'pytest_user@mail.ru',
          'password': 'pytest123',
          'permission': 'USER',
          'username': 'Pytest'
          }, 201)
    ]
)
def test_create_user(data, result, delete_user):

    response_create = create_user_request(data)
    response_get = requests.get(f"http://127.0.0.1:5000/rest/v1/users/{response_create.json().get('id')}",
                                headers={'Authorization': user_login()}).json()

    assert not None == response_get.get('id')

    if response_create:
        delete_user(response_create.json().get('id'))

    assert result == response_create.status_code


def test_validate_user(delete_user):
    user = pytest_user()
    response_create_user = create_user_request(user)

    if response_create_user:
        delete_user(response_create_user.json().get('id'))

    assert None != response_create_user.json().get('id')
    assert 'pytest_user@mail.ru' == response_create_user.json().get('email')
    assert 'USER' == response_create_user.json().get('permission')
    assert 'Pytest_user' == response_create_user.json().get('username')


def test_repeated_create_user(create_and_delete_user):
    user = pytest_user()
    response_create_user = create_user_request(user)

    assert 400 == response_create_user.status_code
