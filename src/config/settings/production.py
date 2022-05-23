from .staging import *

SECRET_KEY = os.environ.get('BACKEND_SECRET_KEY', 'django-secure-rz2zx%7x38d7vw6sy=&93qwyjax@-9#!cu8hjyxy8hj=7)4uz2')

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('BACKEND_DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('BACKEND_DB_NAME', 'backend_db'),
        'USER': os.environ.get('BACKEND_DB_USER', 'backend_user'),
        'PASSWORD': os.environ.get('BACKEND_DB_PASSWORD', 'backend_password'),
        'HOST': os.environ.get('BACKEND_DB_HOST', 'localhost'),
        'PORT': os.environ.get('BACKEND_DB_PORT', 5432)
    }
}


# Caching
# https://docs.djangoproject.com/en/4.0/topics/cache/#setting-up-the-cache

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

USE_X_FORWARDED_HOST = True

USE_X_FORWARDED_PORT = True



ALLOWED_HOSTS = ['statesng.com.ng', 'api.statesng.com.ng', 'cpanel.statesng.com.ng', 'pages.statesng.com.ng', 'www.statesng.com.ng', 'admin.statesng.com.ng']