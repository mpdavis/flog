import datetime

from flask import url_for

from blog import db


class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    markdown_body = db.StringField(required=True)
    html_body = db.StringField(required=True)
    category = db.StringField(max_length=255)

    def get_edit_url(self):
        return url_for('admin.edit-post', slug=self.slug)

    def get_admin_url(self):
        return url_for('admin.view-post', slug=self.slug)

    def __unicode__(self):
        return self.title

    meta = {
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }
