from wtforms import BooleanField
from wtforms import Form
from wtforms import PasswordField
from wtforms import TextField
from wtforms import validators


class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])


class SetupForm(Form):
    username = TextField("Username")
    password = PasswordField("Password")