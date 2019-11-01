"""
DRF Serializers
"""
from rest_framework import serializers

from . import models


# pylint: disable=W0223
# to_internal_value should be overridden but we don't use this to store values
# so we are good here.
class RelatedFieldName(serializers.StringRelatedField):
    "From the related field return name"

    def to_representation(self, value):
        "Just return the name"
        return value.name


class Product(serializers.HyperlinkedModelSerializer):
    "Product Serializer"
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", read_only=True, lookup_field="external_id"
    )
    id = serializers.CharField(source="external_id")
    brand = RelatedFieldName()
    retailer = RelatedFieldName()
    price = serializers.FloatField()

    # pylint: disable=R0903
    # DRF non-conformance
    class Meta:
        "Meta"
        model = models.Product
        fields = ["url", "id", "name", "brand", "retailer", "price", "in_stock"]
