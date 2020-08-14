from .base import *
import os

DEBUG = False

ADMINS = (
    ('Esieboma Jeremiah', 'esiebomaj@gmail.com.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'skillng',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('postgres_password')}
}
