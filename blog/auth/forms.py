from wtforms import BooleanField
from wtforms import Form
from wtforms import PasswordField
from wtforms import TextField
from wtforms import TextAreaField
from wtforms import validators


class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])


class SetupForm(Form):
    username = TextField("Admin Username")
    password = PasswordField("Admin Password")
    author_name = TextField("Author Name")
    author_bio = TextAreaField("Author Bio")
    flog_name = TextField("Flog Name")
    disqus_shortname = TextField("Disqus Shortname")