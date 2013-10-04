import json

from flask import Blueprint
from flask import flash
from flask import render_template
from flask import request
from flask.views import MethodView

from blog.auth.forms import LoginForm
from blog.auth.forms import SetupForm
from blog.auth.models import User
from blog.auth import UserAwareMethodView


auth = Blueprint('auth', __name__, template_folder='templates')


class LoginView(UserAwareMethodView):

    def get(self):
        form = LoginForm()
        return render_template('auth/login.html', form=form)

    def post(self):

        form = LoginForm(request.form)
        logged_in = False
        message = ''

        if form.validate():

            user = User.objects.get(username=form.username.data)

            if user:
                logged_in = user.check_password()
                if not logged_in:
                    message = "Incorrect username or password"
            else:
                message = "Incorrect username or password"

        response = json.dumps(
            {
                'logged_in': logged_in,
                'error_message': message,
            })

        return response


class SetupView(UserAwareMethodView):

    def get(self):
        form = SetupForm()
        return render_template('auth/setup.html', form=form)


# Register the urls
auth.add_url_rule('/login/', view_func=LoginView.as_view('login'))
auth.add_url_rule('/setup/', view_func=SetupView.as_view('setup'))
