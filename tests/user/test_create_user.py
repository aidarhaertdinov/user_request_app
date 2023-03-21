from tests.user.service import pytest_user, request_post
import pytest


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
          }, 400),
        ({'email': 'pytest_user@mail.ru',
          'permission': 'USER',
          'username': 'Pytest_user'
          }, 400)
    ]
)
def test_create_user(data, result, delete_user):
    user = data
    response_create_user = request_post(user)

    if response_create_user:
        delete_user(response_create_user.json().get('id'))

    assert result == response_create_user.status_code


def test_validate_user(delete_user):
    user = pytest_user()
    response_create_user = request_post(user)

    if response_create_user:
        delete_user(response_create_user.json().get('id'))

    assert None != response_create_user.json().get('id')
    assert 'pytest_user@mail.ru' == response_create_user.json().get('email')
    assert 'USER' == response_create_user.json().get('permission')
    assert 'Pytest_user' == response_create_user.json().get('username')


def test_repeated_create_user(create_and_delete_user):
    user = pytest_user()
    response_create_user = request_post(user)

    assert 400 == response_create_user.status_code
