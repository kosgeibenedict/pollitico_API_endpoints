from flask import Flask
from instance.config import app_config
from app.v1.views.parties import api


def createApp():
	app = Flask(__name__)

	app.config.from_pyfile('config.py')
	app.register_blueprint(api)

	return app
