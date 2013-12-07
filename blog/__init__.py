
import os
import settings
import templatetags

from flask import Flask
from flask import redirect
from flask import request
from flask import url_for

# from flask.ext.mongoengine import MongoEngine

from flask.ext.sqlalchemy import SQLAlchemy

from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = settings.SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
db.create_all()


from blog.auth import load_user
from blog.auth import user_unauthorized_callback

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.unauthorized_handler(user_unauthorized_callback)
login_manager.user_loader(load_user)

from blog.auth.models import User


@app.before_first_request
def first_request():
    db.create_all()


@app.before_request
def check_app_state():

    # Don't redirect static files
    if request.path.startswith('/static'):
        return

    if not settings.SETUP_COMPLETE:
        if not request.path == url_for("auth.setup"):
            users = User.query.all()
            if len(users):
                settings.SETUP_COMPLETE = True

            if not settings.SETUP_COMPLETE:
                return redirect(url_for("auth.setup"))

templatetags.setup_jinja2_environment(app)

from admin.views import admin
from auth.views import auth
from posts.views import posts
from projects.views import projects

app.register_blueprint(admin)
app.register_blueprint(auth)
app.register_blueprint(posts)
app.register_blueprint(projects)

