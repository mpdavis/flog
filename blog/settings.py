
import os


SECRET_KEY = "S3CR3T"

MONGODB_DB = ''
MONGODB_HOST = ''
MONGODB_PORT = ''
MONGODB_USERNAME = ''
MONGODB_PASSWORD = ''

ADMIN_EMAIL = 'mike.philip.davis@gmail.com'


try:
    from settingslocal import *
except ImportError:
    pass