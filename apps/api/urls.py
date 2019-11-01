"""
Include this url modul in the main url module.
"""
from rest_framework import routers

from . import views

ROUTER = routers.DefaultRouter()
ROUTER.register("product", views.Product)
ROUTER.register("product_cheapest", views.CheapestProduct, basename="product_cheapest")

# pylint: disable=C0103
# Django non-conformance
urlpatterns = ROUTER.urls
