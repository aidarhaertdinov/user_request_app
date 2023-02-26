from flask import current_app


class BaseRepository:

    BASE_URL = None
    BASE_ENDPOINT = '/rest/v1'
    BASE_ENDPOINT_AUTH = '/auth'
    USERS_URL = '/users'


    def __init__(self, app):
        self.BASE_URL = BaseRepository.calculate_base_url(app)


    @staticmethod
    def calculate_base_url(app):

        BASE_URL = f"{app.config['PROTOCOL_REST_BACKEND']}{app.config['URL_REST_BACKEND']}:" \
                   f"{app.config['PORT_REST_BACKEND']}"
        return BASE_URL


    def create_headers(self):

        return {'Authorization': current_app.config.get('TOKEN')}
