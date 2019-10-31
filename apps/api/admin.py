"""
Django automagically admin hook.
"""
from django.contrib import admin

from . import models


class ProductAdmin(admin.ModelAdmin):
    "Override Product Admin"
    # use raw id fields otherwise the admin site is really slow.
    raw_id_fields = ("brand", "retailer")


admin.site.register(models.Brand)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Retailer)
admin.site.register(models.Source)
