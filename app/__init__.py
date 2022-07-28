from flask_cors import CORS
from flask import Flask


def create_app():
	app = Flask(__name__)
	CORS(app)

	with app.app_context():
		from api import routes
	return app

