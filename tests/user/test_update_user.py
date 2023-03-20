import requests
from tests.user.service import user_login, pytest_user

#
# def test_create_user(delete_user):
#     user = pytest_user()
#     response_create_user = requests.post('http://127.0.0.1:5000/rest/v1/create_user',
#                                          json=user,
#                                          headers={'Authorization': user_login()})
#
#     assert 201 == response_create_user.status_code
#
#     delete_user(response_create_user.json().get('id'))



def test_update_user(create_user_for_update):
    update_user = pytest_user()
    response_update = requests.put(f"http://127.0.0.1:5000/rest/v1/users/{create_user_for_update.json().get('id')}",
                                   json=update_user,
                                   headers={'Authorization': user_login()})

    assert 200 == response_update.status_code

