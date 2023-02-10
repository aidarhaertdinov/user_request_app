from flask import Flask
from config import config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_moment import Moment



login_manager = LoginManager()
bootstrap = Bootstrap()
csrf = CSRFProtect()
moment = Moment()





def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    login_manager.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)
    moment.init_app(app)


    from .main import main
    app.register_blueprint(main)

    from .auth import auth
    app.register_blueprint(auth)

    from app.repository.user_repository import calculate_base_url
    calculate_base_url()

    return app