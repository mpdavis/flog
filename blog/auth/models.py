
from passlib.hash import pbkdf2_sha512

from blog import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(200))

    def __init__(self, username, password):
        self.username = username
        self.password = pbkdf2_sha512.encrypt(password)

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
