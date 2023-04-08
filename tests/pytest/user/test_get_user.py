from tests.pytest.user.service import request_get


def test_positive_get_user(create_and_delete_user):

    response_get = request_get(create_and_delete_user.json().get('id'))

    assert 200 == response_get.status_code
    assert 'pytest_user@mail.ru' == response_get.json().get('email')
    assert 'USER' == response_get.json().get('permission')
    assert 'Pytest_user' == response_get.json().get('username')


def test_negative_get_user(create_and_delete_user):

    response_get = request_get(id='5780')

    assert 400 == response_get.status_code
    assert None == response_get.json().get('email')
    assert None == response_get.json().get('permission')
    assert None == response_get.json().get('username')