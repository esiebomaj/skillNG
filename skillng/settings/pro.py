from .base import *
import os

DEBUG = True

ADMINS = (
    ('Esieboma Jeremiah', 'esiebomaj@gmail.com.com'),
)

ALLOWED_HOSTS = ['*']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'skillng',
#         'USER': 'postgres',
#         'PASSWORD': os.environ.get('postgres_password')}
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
