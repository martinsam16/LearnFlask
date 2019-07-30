from .views import page
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect #Prevencion de suplantacion en forms

app = Flask(__name__)
bootstrap = Bootstrap()
csrf = CSRFProtect()


def create_app(config):
    app.config.from_object(config)

    csrf.init_app(app)
    bootstrap.init_app(app)

    app.register_blueprint(page)
    return app
