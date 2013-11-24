
import settings
import templatetags

from flask import Flask
from flask import redirect
from flask import request
from flask import url_for

from flask.ext.mongoengine import MongoEngine

from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = settings.SECRET_KEY

app.config['MONGODB_DB'] = settings.MONGODB_DB
app.config['MONGODB_HOST'] = settings.MONGODB_HOST
app.config['MONGODB_PORT'] = settings.MONGODB_PORT
app.config['MONGODB_USERNAME'] = settings.MONGODB_USERNAME
app.config['MONGODB_PASSWORD'] = settings.MONGODB_PASSWORD

db = MongoEngine(app)


from blog.auth import load_user
from blog.auth import user_unauthorized_callback

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.unauthorized_handler(user_unauthorized_callback)
login_manager.user_loader(load_user)


from blog.auth.models import User

@app.before_request
def check_app_state():

    if not settings.SETUP_COMPLETE:
        if not request.path == url_for("auth.setup"):
            users = User.objects.all()
            if len(users):
                settings.SETUP_COMPLETE = True

    if not settings.SETUP_COMPLETE:
        print "redirect?"
        redirect("auth.setup")

templatetags.setup_jinja2_environment(app)

from admin.views import admin
from auth.views import auth
from posts.views import posts
from projects.views import projects

app.register_blueprint(admin)
app.register_blueprint(auth)
app.register_blueprint(posts)
app.register_blueprint(projects)

