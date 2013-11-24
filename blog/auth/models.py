
from passlib.hash import pbkdf2_sha512

from blog import db


class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)

    @classmethod
    def hash_password(cls, password):
        return pbkdf2_sha512.encrypt(password)

    def check_password(self, password):
        return pbkdf2_sha512.verify(password, self.password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def is_anonymous(self):
        return False

    def __unicode__(self):
        return self.username

    meta = {
        'indexes': ['username'],
    }


class Settings(db.Document):
    disqus_shortname = db.StringField()
    posts_enabled = db.BooleanField()

    @classmethod
    def create(cls):
        settings = Settings.objects.all()

