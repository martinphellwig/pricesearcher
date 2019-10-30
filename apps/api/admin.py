"""
Django automagically admin hook.
"""
from django.contrib import admin

from . import models

admin.site.register(models.Brand)
admin.site.register(models.Product)
admin.site.register(models.Retailer)
admin.site.register(models.Source)
