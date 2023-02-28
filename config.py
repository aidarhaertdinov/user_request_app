import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    PROTOCOL_REST_BACKEND = os.getenv('PROTOCOL_REST_BACKEND')
    URL_REST_BACKEND = os.getenv('URL_REST_BACKEND')
    PORT_REST_BACKEND = os.getenv('PORT_REST_BACKEND')
    SECRET_KEY = os.getenv('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
    TOKEN = os.getenv('TOKEN')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/user_request_app'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production.db'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
