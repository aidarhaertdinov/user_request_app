import requests


def test_index():
    def create_user(self, user) -> User:
        return User.from_json(requests.post(f"{BaseRepository.calculate_base_url(current_app)}"
                                            f"{BaseRepository.BASE_ENDPOINT}/create_user",
                                            json=user,
                                            headers=BaseRepository.get_authorization_headers(self))
                              .json()
                              )
    user = {'email': 'admin@mail.ru',
            'password': '123'
            }
    response = requests.post('http://127.0.0.1:5000/auth/login', json=user)
    assert 201 == response.status_code









