from flask import Flask, jsonify, after_this_request
import models
import os
from flask_cors import CORS
from flask_login import LoginManager

from dotenv import load_dotenv
load_dotenv()

from resources.seeds import seeds
from resources.users import users
from resources.myseeds import myseeds

DEBUG=True
PORT=8000

app = Flask(__name__)
CORS(app)

app.secret_key = os.environ.get("FLASK_APP_SECRET")
app.config['SESSION_COOKIE_SAMESITE'] = "None"
app.config['SESSION_COOKIE_SECURE'] = True
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

CORS(seeds, origins=['http://localhost:3000', 'https://sown-app.herokuapp.com/'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000', 'https://sown-app.herokuapp.com/'], supports_credentials=True)
CORS(myseeds, origins=['http://localhost:3000', 'https://sown-app.herokuapp.com/'], supports_credentials=True)

app.register_blueprint(seeds, url_prefix='/api/v1/seeds')
app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(myseeds, url_prefix='/api/v1/myseeds')

@app.before_request
def before_request():

    """Connect to the db before each request"""
    print("you should see this before each request")
    models.DATABASE.connect()

    @after_this_request
    def after_request(response):
        """Close the db connetion after each request"""
        print("you should see this after each request")
        models.DATABASE.close()
        return response

if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.initialize()

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)