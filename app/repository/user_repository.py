from ..model import User
from flask import current_app
import requests
from ..security.decorators import decorator_function
from .base_repository import BaseRepository


class UserRepository(BaseRepository):


    def user_login(self, user) -> bool:
        if user:
            data = requests.post(f"{BaseRepository.calculate_base_url(current_app)}"
                                 f"{BaseRepository.BASE_ENDPOINT_AUTH}/login",
                                 json=user) \
                .json()

            current_app.config['TOKEN'] = f"Bearer {data['token']}"
            return True
        else:
            return False

    def create_user(self, user) -> User:
        return User.from_json(requests.post(f"{BaseRepository.calculate_base_url(current_app)}"
                                            f"{BaseRepository.BASE_ENDPOINT}/create_user",
                                            json=user,
                                            headers=BaseRepository.create_headers(self))
                              .json()
                              )

    @decorator_function
    def get_users(self) -> list[User]:
        list_users = requests.get(f"{BaseRepository.calculate_base_url(current_app)}"
                                  f"{BaseRepository.BASE_ENDPOINT}{BaseRepository.USERS_URL}",
                                  headers=BaseRepository.create_headers(self)) \
            .json()
        users = [User.from_json(user) for user in list_users]
        return users

    def get_user(self, id: int) -> User:
        return User.from_json(requests.get(f"{BaseRepository.calculate_base_url(current_app)}"
                                           f"{BaseRepository.BASE_ENDPOINT}{BaseRepository.USERS_URL}"
                                           f"/{id}",
                                           headers=BaseRepository.create_headers(self))
                              .json()
                              )

    def put_user(self, id: int, update_user) -> User:
        return User.from_json(requests.put(f"{BaseRepository.calculate_base_url(current_app)}"
                                           f"{BaseRepository.BASE_ENDPOINT}{BaseRepository.USERS_URL}/{id}",
                                           json=update_user,
                                           headers=BaseRepository.create_headers(self))
                              .json()
                              )

    def delete_user(self, id: int) -> User:
        return User.from_json(requests.delete(f"{BaseRepository.calculate_base_url(current_app)}"
                                              f"{BaseRepository.BASE_ENDPOINT}{BaseRepository.USERS_URL}/{id}",
                                              headers=BaseRepository.create_headers(self))
                              .json()
                              )
