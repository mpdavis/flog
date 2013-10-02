from flask import Flask
from flask.ext.mongoengine import MongoEngine

import settings


app = Flask(__name__)

app.config['SECRET_KEY'] = settings.SECRET_KEY

app.config['MONGODB_DB'] = settings.MONGODB_DB
app.config['MONGODB_HOST'] = settings.MONGODB_HOST
app.config['MONGODB_PORT'] = settings.MONGODB_PORT
app.config['MONGODB_USERNAME'] = settings.MONGODB_USERNAME
app.config['MONGODB_PASSWORD'] = settings.MONGODB_PASSWORD

db = MongoEngine(app)


from admin.views import admin
from pages.views import pages
from posts.views import posts

app.register_blueprint(admin)
app.register_blueprint(pages)
app.register_blueprint(posts)

