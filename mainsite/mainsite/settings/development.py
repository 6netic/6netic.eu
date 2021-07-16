from .base import *


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'default_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '5432',
    },
    'purbeurre': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'other_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '5432',
    }
}
