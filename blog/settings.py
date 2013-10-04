
import os


SETUP_COMPLETE = False
SETUP_IN_PROGRESS = False

SECRET_KEY = "S3CR3T"

MONGODB_DB = os.environ.get('MONGODB_DB', None)
MONGODB_HOST = os.environ.get('MONGODB_HOST', None)
MONGODB_PORT = os.environ.get('MONGODB_PORT', 47458)
MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME', None)
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD', None)

ADMIN_EMAIL = 'mike.philip.davis@gmail.com'
ADMIN_NAME = 'Michael Davis'


try:
    from settingslocal import *
except ImportError:
    pass