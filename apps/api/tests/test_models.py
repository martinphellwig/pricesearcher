"""
Test Cases for models
"""

from django.test import TestCase

from . import factories


class TestFetch(TestCase):
    "Test cases for models"

    def test_1_source_str(self):
        "Does it return a string."
        subject = factories.SourceFactory
        instance = subject()
        expected = instance.name
        returned = str(instance)
        self.assertEqual(expected, returned)

    def test_2_brand_str(self):
        "Does it return a string."
        subject = factories.BrandFactory
        instance = subject()
        expected = instance.name
        returned = str(instance)
        self.assertEqual(expected, returned)

    def test_3_retailer_str(self):
        "Does it return a string."
        subject = factories.RetailerFactory
        instance = subject()
        expected = instance.name
        returned = str(instance)
        self.assertEqual(expected, returned)

    def test_4_product_str(self):
        "Does it return a string."
        subject = factories.ProductFactory
        instance = subject()
        expected = "{} - {} - {}".format(
            instance.name, instance.brand, instance.retailer
        )
        returned = str(instance)
        self.assertEqual(expected, returned)
