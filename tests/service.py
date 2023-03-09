

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