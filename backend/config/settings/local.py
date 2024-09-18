import logging
import sys

from .base import *
from .base import env

DEBUG = True
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


# DEBUG TOOLBAR
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

INSTALLED_APPS += ["django_extensions"]

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "SIMPLE %(levelname)s %(asctime)s %(message)s"
        }
    },
    "handlers": {
        "console_simple": {
            "level": logging.INFO,
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "simple",
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["console_simple"],
            "level": "INFO",
            "propagate": True,
        },
    }
}
