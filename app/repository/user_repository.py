
from ..model import User
from config import Config
from flask import current_app, g, session
import requests


BASE_URL = None
BASE_ENDPOINT = '/rest/v1'


def calculate_base_url(app):
    global BASE_URL
    BASE_URL = f"{app.config['PROTOCOL_REST_BACKEND']}{app.config['URL_REST_BACKEND']}:{app.config['PORT_REST_BACKEND']}"

def user_registration(user) -> User:
    return User.from_json(requests.post(f"{BASE_URL}{BASE_ENDPOINT}/registration", json=user).json())

def user_login(user) -> bool:
    if user:
        data = requests.post(f"{BASE_URL}{BASE_ENDPOINT}/login", json=user).json()
        current_app.config[ 'token'] = f"Bearer {data['token']}"
        # session['token'] = f"Bearer {data['token']}"
        return True
    else:
        return False

# TODO сделать привидение типа User
def get_all_users() -> list[User]:

    list_users = requests.get(f"{BASE_URL}{BASE_ENDPOINT}/users", headers={'Authorization':current_app.config['token']}).json()

    users = [User.from_json(user) for user in list_users]
    return users


def get_user(id:int) -> User:
    return User.from_json(requests.get(f"{BASE_URL}{BASE_ENDPOINT}/users/{id}", headers={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzIsImV4cCI6MTY3NzI2MzQ3M30.-agU5G67EJsDx4pNDfBEu9mSNop0WmUjN0C9kjMd7Y0'}).json())


def put_user(id:int, update_user) -> User:
    return User.from_json(requests.put(f"{BASE_URL}{BASE_ENDPOINT}/users/{id}", json=update_user).json())


def delete_user(id:int) -> User:
    return User.from_json(requests.delete(f"{BASE_URL}{BASE_ENDPOINT}/users/{id}").json())






