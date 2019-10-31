"""
Models that hold the ingested data.
"""

from django.db import models
from django.utils.text import slugify

# pylint: disable=C0115, R0903
# warning for docstring for meta classes and too few methods, not applicable for
# django usage.


class SlugNameBase(models.Model):
    "This Abstract model will set the slug field from the name."
    name = models.CharField(max_length=64, blank=True, null=True)
    slug = models.SlugField(max_length=64, blank=True, null=True, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)

    # pylint: disable=C0330
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        "Original save method called and returned at end."
        self.slug = slugify(self.name)
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )


class Source(models.Model):
    "Import Source"
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Brand(SlugNameBase):
    "The Brand"


class Retailer(SlugNameBase):
    "The Retailer"


class Product(models.Model):
    "Product"
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=16)
    name = models.CharField(max_length=64, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=8)
    in_stock = models.BooleanField(null=True)

    class Meta:
        unique_together = [["external_id", "name", "brand", "retailer"]]

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.brand, self.retailer)
