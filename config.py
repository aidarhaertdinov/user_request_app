import os


# TODO os.getenv
class Config:
    PROTOCOL_REST_BACKEND = os.getenv('PROTOCOL_REST_BACKEND') or 'http://'
    URL_REST_BACKEND = os.getenv('URL_REST_BACKEND') or '127.0.0.1'
    PORT_REST_BACKEND = os.getenv('PORT_REST_BACKEND') or '5000'
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(32)
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY') or os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or False


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