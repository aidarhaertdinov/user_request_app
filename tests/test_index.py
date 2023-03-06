import requests


def test_index():
    user = {'email': 'admin@mail.ru',
            'password': '123'
            }
    response = requests.post('http://127.0.0.1:5000/auth/login', json=user)
    assert 201 == response.status_code







