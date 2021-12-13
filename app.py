from flask import Flask
import models

from resources.seeds import seeds

DEBUG=True
PORT=8000

app = Flask(__name__)

app.register_blueprint(seeds, url_prefix='/api/v1/seeds')

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)