"""
DRF views.
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from . import models, serializers

# pylint: disable=R0901, E1101
# DRF & Django non-conformance


class _Base(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    "Base Product view"
    lookup_field = "external_id"
    serializer_class = serializers.Product


class Product(_Base):
    "Product View"
    queryset = models.Product.objects.all().order_by("name")


class CheapestProduct(_Base):
    "Cheapest Product View"
    queryset = models.Product.objects.filter(price__isnull=False).order_by(
        "price", "name", "brand__slug", "retailer__slug"
    )
