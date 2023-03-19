import pytest
import requests
from tests.integration.service import user_login
from tests.integration.test_user import test_create_user


# @pytest.fixture()
# def create_user():
#     user = {'email': 'pytest_user@mail.ru',
#             'password': 'pytest123',
#             'permission': 'USER',
#             'username': 'Pytest_user'
#             }
#     response_create_user = requests.post('http://127.0.0.1:5000/rest/v1/create_user',
#                                          json=user,
#                                          headers={'Authorization': user_login()})
#     return response_create_user
#
#
# @pytest.fixture()
# def create_user_for_update():
#     user = {'email': 'pytest_user@mail.ru',
#             'password': 'pytest123',
#             'permission': 'USER',
#             'username': 'Py'
#             }
#     response_create_user = requests.post('http://127.0.0.1:5000/rest/v1/create_user',
#                                          json=user,
#                                          headers={'Authorization': user_login()})
#
#     yield response_create_user
#
#     requests.delete(f"http://127.0.0.1:5000/rest/v1/users/{response_create_user.json().get('id')}",
#                     headers={'Authorization': user_login()})
#

@pytest.fixture()
def delete_user(request):

    yield

    requests.delete(f"http://127.0.0.1:5000/rest/v1/users/{request}",
                    headers={'Authorization': user_login()})

