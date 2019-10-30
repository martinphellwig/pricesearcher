"""
Apps module is the default Django module to hold the Config class.
"""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    "Django Application Configuration for API."
    name = "api"
    verbose_name = "API"
