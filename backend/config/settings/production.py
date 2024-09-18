from .base import *
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

# DATABASES
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

# ADMIN
ADMIN_URL = env("DJANGO_ADMIN_URL")

# LOGGING
REQUEST_LOGGING_ENABLE_COLORIZE = False
