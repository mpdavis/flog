from flask import Blueprint, render_template
from flask.views import MethodView

from blog.auth.models import User


auth = Blueprint('auth', __name__, template_folder='templates')


class LoginView(MethodView):

    def get(self):
        return render_template('auth/login.html')


# Register the urls
auth.add_url_rule('/login/', view_func=LoginView.as_view('login'))
