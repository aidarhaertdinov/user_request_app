import unittest
from unittest import TestCase
import requests
from app import create_app
from app.repository.user_repository import UserRepository
from main import app
from tests.pytest.user.service import user_login


class UpdateUserTestCase(TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.user_repository = app.user_repository

        user = {'email': 'unittest_user@mail.ru',
                'password': 'unittest123',
                'permission': 'USER',
                'username': 'Unittest_user'
                }
        self.response_user = requests.post(f"http://127.0.0.1:5000/rest/v1/create_user",
                                           json=user,
                                           headers={'Authorization': user_login()}).json()

    def tearDown(self):
        requests.delete(f"http://127.0.0.1:5000/rest/v1/users/{self.response_user.get('id')}",
                        headers={'Authorization': user_login()}).json()

    def test_update_user(self):
        update_user = {
            'email': 'unittest_user@mail.ru',
            'password': 'unittest123',
            'permission': 'MODERATE',
            'username': 'Unittest'
        }

        with create_app().app_context():
            self.response_update_user = requests.put(
                f"http://127.0.0.1:5000/rest/v1/users/{self.response_user.get('id')}",
                json=update_user,
                headers={'Authorization': user_login()}).json()

            assert not None == self.response_update_user.get('id')
            assert 'unittest_user@mail.ru' == self.response_update_user.get('email')
            assert 'MODERATE' == self.response_update_user.get('permission')
            assert 'Unittest' == self.response_update_user.get('username')


if __name__ == '__main__':
    unittest.main()
