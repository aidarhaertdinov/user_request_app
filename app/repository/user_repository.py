from ..model import User
from config import Config
from flask import current_app
import requests


BASE_URL = None
BASE_ENDPOINT = '/rest/v1'

# This typically means that you attempted to use functionality that needed
# the current application. To solve this, set up an application context
# with app.app_context(). See the documentation for more information.

# def calculate_base_url():
#     global BASE_URL
#     BASE_URL = f"{current_app.config['PROTOCOL_REST_BACKEND']}{current_app.config['URL_REST_BACKEND']}:{current_app.config['PORT_REST_BACKEND']}"


def calculate_base_url():
    global BASE_URL
    BASE_URL = (f"{Config.PROTOCOL_REST_BACKEND}{Config.URL_REST_BACKEND}:{Config.PORT_REST_BACKEND}")


# TODO сделать привидение типа User
def get_all_users() -> User:
    return requests.get(f"{BASE_URL}{BASE_ENDPOINT}/users").json()


def get_user(id:int) -> User:
    return User.from_json(requests.get(f"{BASE_URL}{BASE_ENDPOINT}/users/{id}").json())


def put_user(id:int, update_user) -> User:
    return requests.put(f"{BASE_URL}{BASE_ENDPOINT}/users/{id}", json=update_user)


def delete_user(id:int) -> User:
    return requests.delete(f"{BASE_URL}{BASE_ENDPOINT}/users/{id}")


def login_user(user) -> User:
    return requests.post(f"{BASE_URL}{BASE_ENDPOINT}/login", json=user).json()


def registration_user(user) -> User:
    return requests.post(f"{BASE_URL}{BASE_ENDPOINT}/registration", json=user)
