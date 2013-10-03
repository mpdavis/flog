
from passlib.hash import pbkdf2_sha512

from blog import db


class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)

    def hash_password(self, password):
        return pbkdf2_sha512.encrypt(password)

    def check_password(self, password):
        return pbkdf2_sha512.decrypt(password, self.password)

    def __unicode__(self):
        return self.username

    meta = {
        'indexes': ['username'],
    }

