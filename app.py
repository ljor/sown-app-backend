from flask import Flask, jsonify
import models
import os
from flask_cors import CORS
from flask_login import LoginManager, login_manager

from dotenv import load_dotenv
load_dotenv()

from resources.seeds import seeds
from resources.users import users

DEBUG=True
PORT=8000

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_APP_SECRET")
login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    try:
        print("loading the following user")
        user = models.User.get_by_id(user_id)
        return user
    except models.DoesNotExist:
        return None

@login_manager.unauthorized_handler
def unauthorized():
    return jsonify(
        data={
            'error': 'User not logged in'
        },
        message="You must be logged in to ccass that resource",
        status=401
    ), 401

CORS(seeds, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(seeds, url_prefix='/api/v1/seeds')
app.register_blueprint(users, url_prefix='/api/v1/users')

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)