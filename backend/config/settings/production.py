import logging
import sys

from .base import *
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# DATABASES
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

# ADMIN
ADMIN_URL = env("DJANGO_ADMIN_URL")

MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# LOGGING
REQUEST_LOGGING_ENABLE_COLORIZE = False
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(pathname)s %(funcName)s %(message)s"
        },
        "simple": {
            "format": "%(levelname)s %(asctime)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": logging.INFO,
            "class": "logging.StreamHandler",
            "stream": sys.stderr,
            "formatter": "verbose"
        },
        "console_simple": {
            "level": logging.INFO,
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "simple",
        }
    },
    "loggers": {
        "django.db.backends": {
            "level": logging.ERROR,
            "handlers": ["console"],
            "propagate": False,
        },
        "django.security.DisallowedHost": {
            "level": logging.ERROR,
            "handlers": ["console"],
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console_simple"],
            "level": logging.INFO,
            "propagate": False
        },
    },
}

