from .base import *

SECRET_KEY = "MySecretKey"

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': '',
		'USER': 'postgres',
		'PASSWORD': '',
		'HOST': '',
		'PORT': '',
	},
}