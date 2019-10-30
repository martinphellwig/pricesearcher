"""
Models that hold the ingested data.
"""

from django.db import models

# pylint: disable=C0115, R0903
# warning for docstring for meta classes and too few methods, not applicable for
# django usage.

class Source(models.Model):
    "Import Source"
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    "The Brand"
    name = models.CharField(max_length=64, blank=True, null=True)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Retailer(models.Model):
    "The Retailer"
    name = models.CharField(max_length=64, blank=True, null=True)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    "Product"
    external_id = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=8)
    in_stock = models.BooleanField(null=True)

    class Meta:
        unique_together = [["external_id", "name", "brand", "retailer"]]

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.brand, self.retailer)
