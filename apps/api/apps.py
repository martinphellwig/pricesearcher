"""
Apps module is the default Django module to hold the Config class.
"""
import os

from django.apps import AppConfig


def _ready():
    "called by appconfig ready"
    if os.environ.get("RUN_MAIN", "false") == "true":
        from .lib import import_json

        import_json.fetch_and_store()
        return True

    return False


class ApiConfig(AppConfig):
    "Django Application Configuration for API."
    name = "apps.api"
    verbose_name = "API"

    def ready(self):
        _ready()
