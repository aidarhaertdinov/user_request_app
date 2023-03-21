from tests.user.service import request_put
import pytest


@pytest.mark.parametrize(
    "data, result",
    [
        ({'email': 'pytest_user@mail.ru',
          'password': 'pytest123',
          'permission': 'USER',
          'username': 'PYTEST'
          }, 200),
        ({'email': 'pytest_user@mail.ru',
          'password': 'pytest123',
          'permission': 'MODERATE',
          'username': 'Pytest_user'
          }, 200),
        ({'email': 'pytest_user@mail.ru',
          'password': '123TEST123',
          'permission': 'USER',
          'username': 'Pytest_user'
          }, 200)
    ]
)
def test_update_user(data, result, create_and_delete_user):
    response_update = request_put(data, create_and_delete_user.json().get('id'))

    assert result == response_update.status_code


def test_validate_update_user(create_and_delete_user):
    update_user = {'email': 'pytest_user@mail.ru',
                   'password': 'pytest123',
                   'permission': 'USER',
                   'username': 'Update_pytest_user'
                   }
    response_update = request_put(update_user, create_and_delete_user.json().get('id'))

    assert None != response_update.json().get('id')
    assert 'pytest_user@mail.ru' == response_update.json().get('email')
    assert 'USER' == response_update.json().get('permission')
    assert 'Update_pytest_user' == response_update.json().get('username')
