import datetime

from flask import url_for

from blog import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    title = db.Column(db.String(240))
    slug = db.Column(db.String(240))
    markdown_body = db.Column(db.String(10000))
    html_body = db.Column(db.String(10000))

    def get_edit_url(self):
        return url_for('admin.edit-post', slug=self.slug)

    def get_admin_url(self):
        return url_for('admin.view-post', slug=self.slug)
