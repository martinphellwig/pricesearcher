"""
Factories as used by factory boy.
"""
import factory

from .. import models

# pylint: disable=C0115, R0903, W0108
# docstring for meta classes, too few methods and warning for unnecessary lambda
# warnings are not applicable here.


class SourceFactory(factory.django.DjangoModelFactory):
    "Factory for the Source model."

    class Meta:
        model = models.Source

    name = factory.Sequence(lambda sequence: "Import from #{}".format(sequence))


class BrandFactory(factory.django.DjangoModelFactory):
    "Factory for the Brand model."

    class Meta:
        model = models.Brand

    name = factory.Sequence(lambda sequence: "Brand Name #{}".format(sequence))


class RetailerFactory(factory.django.DjangoModelFactory):
    "Factory for the Retailer model."

    class Meta:
        model = models.Retailer

    name = factory.Sequence(lambda sequence: "Retailer #{}".format(sequence))


class ProductFactory(factory.django.DjangoModelFactory):
    "Factory for the Product model."

    class Meta:
        model = models.Product

    external_id = factory.Sequence(lambda sequence: "{}".format(sequence))
    name = factory.Sequence(lambda sequence: "Retailer #{}".format(sequence))
    brand = factory.SubFactory(BrandFactory)
    retailer = factory.SubFactory(RetailerFactory)


def reset():
    "Rest sequences for all factories."
    factories = [SourceFactory, BrandFactory, RetailerFactory, ProductFactory]
    for model_factory in factories:
        model_factory.reset_sequence()
