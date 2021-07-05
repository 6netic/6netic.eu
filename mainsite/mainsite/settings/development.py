from .base import *


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'booking_db',
        'USER': 'brestoche',
        'PASSWORD': 'BerHAuSs039',
        'HOST': '',
        'PORT': '5432',
    }
}
