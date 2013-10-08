from wtforms import Form
from wtforms import TextAreaField
from wtforms import TextField
from wtforms import validators


class NewPostForm(Form):
    title = TextField('Title', [validators.Required()])
    slug = TextField('Slug', [validators.Required()])
    body = TextAreaField('Body', [validators.Required()])


class NewProjectForm(Form):
    title = TextField('Title', [validators.Required()])
    subtitle = TextField('Subtitle', [validators.Required()])
    slug = TextField('Slug', [validators.Required()])
    body = TextAreaField('Body', [validators.Required()])