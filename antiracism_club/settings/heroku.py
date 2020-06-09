import dj_database_url
import os
import sys

from .base import *  # noqa


# DATABASE CONFIGURATION
# -----------------------------------------------------------------------------

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# SECURITY CONFIGURATION
# -----------------------------------------------------------------------------

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True


# ALLOWED_HOSTS CONFIGURATION
# -----------------------------------------------------------------------------

ALLOWED_HOSTS = ['antiracism-club-staging.herokuapp.com',
                 'antiracism-club.herokuapp.com']

# This allows us to include review apps in ALLOWED_HOSTS even though we don't
# know their name until runtime.
APP_NAME = os.environ.get('HEROKU_APP_NAME')
if APP_NAME:
    url = '{}.herokuapp.com'.format(APP_NAME)
    ALLOWED_HOSTS.append(url)


# STATIC FILE CONFIGURATION
# -----------------------------------------------------------------------------

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE += ('whitenoise.middleware.WhiteNoiseMiddleware',)

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# LOGGING CONFIGURATION
# -----------------------------------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'brief': {
            'format': '%(asctime)s %(levelname)s %(name)s[%(funcName)s]: %(message)s',  # noqa
        },
    },
    'handlers': {
        'console_info': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
    },
    'loggers': {
        '': {
            'handlers': ['console_info'],
            'level': 'INFO',
        }
    }
}
