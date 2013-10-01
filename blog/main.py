from flask import Flask
from flask.ext.mongoengine import MongoEngine

import settings

app = Flask(__name__)

app.config['SECRET_KEY'] = settings.SECRET_KEY
app.config["MONGODB_SETTINGS"] = settings.MONGODB_SETTINGS

db = MongoEngine(app)

@app.route('/')
def index():
    return "Test"


if __name__ == '__main__':
    app.run(debug=True)


