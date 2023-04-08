import pytest
from tests.pytest.user.service import create_user_request, request_delete


@pytest.fixture()
def create_and_delete_user():
    user = {'email': 'pytest_user@mail.ru',
            'password': 'pytest123',
            'permission': 'USER',
            'username': 'Pytest_user'
            }
    response_create_user = create_user_request(user)

    yield response_create_user

    request_delete(response_create_user.json().get('id'))


@pytest.fixture()
def delete_user():
    return response_delete_user


def response_delete_user(id):
    response_delete = request_delete(id)

    return response_delete



@pytest.fixture()
def create_user():
    user = {'email': 'pytest_user@mail.ru',
            'password': 'pytest123',
            'permission': 'USER',
            'username': 'Pytest_user'
            }
    response_create_user = create_user_request(user)

    yield response_create_user
