from wtforms import BooleanField
from wtforms import Form
from wtforms import PasswordField
from wtforms import TextField
from wtforms import validators


class LoginForm(Form):
    username = TextField('Username', [validators.Required(), validators.Email()])
    password = PasswordField('Password', [validators.Required()])
    # remember_me = BooleanField('Remember')


class SetupForm(Form):
    text = PasswordField("Text")