
from blog import db

GLOBAL_SETTINGS_OBJECT = 'GLOBAL_SETTINGS_OBJECT'


class GlobalSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flog_name = db.Column(db.String(240))
    disqus_shortname = db.Column(db.String(240))
    posts_enabled = db.Column(db.Boolean)
    author_name = db.Column(db.String(240))
    author_bio = db.Column(db.String(1000))

    @classmethod
    def get_global_settings_object(cls):
        settings = cls.query.filter_by(id=1).first()
        if not settings:
            settings = cls(id=1)
            db.session.add(settings)
            db.session.commit()
        return settings
