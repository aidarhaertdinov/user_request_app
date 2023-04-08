from tests.pytest.user.service import request_delete


def test_positive_delete_user(create_user):

    response_delete = request_delete(create_user.json().get('id'))

    assert 200 == response_delete.status_code
    assert 'pytest_user@mail.ru' == response_delete.json().get('email')
    assert 'USER' == response_delete.json().get('permission')
    assert 'Pytest_user' == response_delete.json().get('username')



def test_negative_delete_user():

    response_delete = request_delete(id='5320')

    assert 400 == response_delete.status_code
    assert None == response_delete.json().get('email')
    assert None == response_delete.json().get('permission')
    assert None == response_delete.json().get('username')