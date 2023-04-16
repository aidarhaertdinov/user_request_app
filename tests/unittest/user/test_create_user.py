import unittest
from unittest import TestCase
import requests
from app import create_app
from app.repository.user_repository import UserRepository
from main import app
from tests.pytest.user.service import user_login


class CreateUserTestCase(TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.user_repository = app.user_repository

    def tearDown(self):
        requests.delete(f"http://127.0.0.1:5000/rest/v1/users/{self.response_create_user.id}",
                        headers={'Authorization': user_login()}).json()

    def test_create_user(self):
        user = {'email': 'unittest_user@mail.ru',
                'password': 'unittest123',
                'permission': 'USER',
                'username': 'Unittest_user'
                }

        with create_app().app_context():
            self.response_create_user = self.user_repository.create_user(user)

            assert not None == self.response_create_user.id
            assert 'unittest_user@mail.ru' == self.response_create_user.email
            assert 'USER' == self.response_create_user.permission
            assert 'Unittest_user' == self.response_create_user.username
            self.assertEqual('Unittest_user', self.response_create_user.username)


if __name__ == '__main__':
    unittest.main()
