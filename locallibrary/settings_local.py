from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

SECRET_KEY = '0xa8db!$tcw7-nfmy+^jem%bptyp9pgj_bmt2ni&!0hz2aa2r5'

ALLOWED_HOSTS = ['192.168.1.10', '127.0.0.1']


STATIC_ROOT = '/home/tconsta/dev/dja/locallibrary/static/'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}