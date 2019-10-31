"""
Test Cases for import store
"""

import io
from unittest import mock

from django.test import TestCase

from ..lib.import_store import store
from ..models import Product

DATA = {
    "id": "1",
    "name": "a name",
    "brand": "a brand",
    "retailer": "a retailer",
    "in_stock": True,
    "price": "1",
}

# pylint: disable=E1101
# False positive, Classes of models do have objects member
class TestJson(TestCase):
    "Test cases for import store"

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    @mock.patch("sys.stderr", new_callable=io.StringIO)
    def test_1_fetch_and_store_quite(self, mock_stderr, mock_stdout):
        "Does it not smoke."
        resource = "test source"
        verbose = False
        store(resource, [DATA], verbose)
        self.assertEqual(Product.objects.all().count(), 1)
        self.assertEqual(mock_stderr.getvalue(), "")
        self.assertEqual(mock_stdout.getvalue(), "")

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    @mock.patch("sys.stderr", new_callable=io.StringIO)
    def test_2_reimport(self, mock_stderr, mock_stdout):
        "If I import it twice do I still have just 1 product."
        resource = "test source"
        verbose = True
        store(resource, [DATA], verbose)
        store(resource, [DATA], verbose)
        self.assertEqual(Product.objects.all().count(), 1)
        self.assertIn("it/s", mock_stderr.getvalue())
        self.assertIn("Storing", mock_stdout.getvalue())

    def test_3_price_is_empty(self):
        "If price is empty it should be set to None"
        resource = "test source"
        verbose = False
        data = DATA.copy()
        data["price"] = ""
        store(resource, [data], verbose)
        product = Product.objects.get()
        self.assertIsNone(product.price)

    def test_4_dequote(self):
        "Strings that are double quoted should be sanitised."
        resource = "test source"
        verbose = False
        data = DATA.copy()

        expected = "double quoted"
        data["name"] = "'{}'".format(expected)
        store(resource, [data], verbose)
        product = Product.objects.get()
        self.assertEqual(product.name, expected)

        expected = "double quoted"
        data["name"] = '"{}"'.format(expected)
        store(resource, [data], verbose)
        product = Product.objects.get()
        self.assertEqual(product.name, "double quoted")

    def test_5_key_rename(self):
        "in stock key shoudl be renamed"
        resource = "test source"
        verbose = False
        data = DATA.copy()
        data.pop("in_stock")
        data["instock"] = False
        store(resource, [data], verbose)
        product = Product.objects.get()
        self.assertFalse(product.in_stock)

    def test_5_missing_key(self):
        "If a key is missing it should be added with none value"
        resource = "test source"
        verbose = False
        data = DATA.copy()
        data.pop("in_stock")
        store(resource, [data], verbose)
        product = Product.objects.get()
        self.assertIsNone(product.in_stock)

    def test_6_boolean_conversion_y(self):
        "Is boolean conversion reasonably fuzzy."
        resource = "test source"
        verbose = False
        data = DATA.copy()
        data["in_stock"] = "yep"
        store(resource, [data], verbose)
        product = Product.objects.get()
        self.assertTrue(product.in_stock)

    def test_7_boolean_conversion_n(self):
        "Is boolean conversion reasonably fuzzy."
        resource = "test source"
        verbose = False
        data = DATA.copy()
        data["in_stock"] = "NoPe"
        store(resource, [data], verbose)
        product = Product.objects.get()
        self.assertFalse(product.in_stock)

    def test_8_boolean_conversion_unknown(self):
        "Is boolean conversion reasonably fuzzy."
        resource = "test source"
        verbose = False
        data = DATA.copy()
        data["in_stock"] = "invalid"
        store(resource, [data], verbose)
        product = Product.objects.get()
        self.assertIsNone(product.in_stock)
