
from flask import session
from flask.views import MethodView

import flask_login

from blog.auth.models import User

from blog import settings


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
            'user': self.user,
            'active_nav': self.active_nav,
        }
        if extra_ctx:
            ctx.update(extra_ctx)
        ctx.update(kwargs)
        return ctx