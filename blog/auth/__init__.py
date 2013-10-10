from functools import wraps

from flask import abort
from flask import redirect
from flask import session
from flask import url_for
from flask.views import MethodView

import flask_login

from blog.auth.models import User

from blog import settings


def user_unauthorized_callback():
    return redirect(url_for('auth.login'))


def load_user(username):
    return User.objects.get(username=username)


class UserAwareMethodView(MethodView):

    @property
    def session(self):
        return session

    @property
    def user(self):
        if not flask_login.current_user.is_anonymous():
            return flask_login.current_user._get_current_object()
        else:
            return None

    def get_context(self, extra_ctx=None, **kwargs):
        ctx = {
            'user':                 self.user,
            'active_nav':           self.active_nav,
            'disqus_shortname':     settings.DISQUS_SHORTNAME,
        }
        if extra_ctx:
            ctx.update(extra_ctx)
        ctx.update(kwargs)
        return ctx


def setup_incomplete(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        users = User.objects.all()
        if len(users):
            abort(404)
        return f(*args, **kwargs)
    return decorated_function