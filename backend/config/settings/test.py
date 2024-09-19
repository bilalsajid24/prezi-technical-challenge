from .base import *
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY")
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# TEMPLATES
TEMPLATES[-1]["OPTIONS"]["loaders"] = [
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

REST_FRAMEWORK["PAGE_SIZE"] = 2
