"""
Test Cases for json import
"""
import io
from unittest import mock

from django.core.management.base import CommandError
from django.test import TestCase

from ..lib.import_json import fetch_and_store


class MockResponse:
    "Mocked Requests response"

    def __init__(self, url):
        self.url = url
        self.status_code = 200
        self.json_data = []

    def raise_for_status(self):
        "dummy function"

    def close(self):
        "dummy function"

    def json(self):
        "dummy function"
        return self.json_data


def mock_get(url):
    "Mock Request get function"
    return MockResponse(url)


def mock_get_404(url):
    "Mock Request get function"
    response = MockResponse(url)
    response.status_code = 404
    return response


MOCK_STORE = "apps.api.lib.import_store.store"

# pylint: disable=R0201
# Did not use any 'self' in the tests, blame unittest for that ;-)
class TestJson(TestCase):
    "Test cases for import json"

    @mock.patch("requests.get", new=mock_get)
    def test_1_fetch_and_store_quite(self):
        "Does it not smoke."
        fetch_and_store(verbose=False)

    @mock.patch("requests.get", new=mock_get)
    @mock.patch("sys.stdout", new_callable=io.StringIO)
    @mock.patch("sys.stderr", new_callable=io.StringIO)
    def test_2_fetch_and_store_verbose(self, mock_stderr, mock_stdout):
        "Does it not smoke."
        fetch_and_store()
        self.assertIn("Done", mock_stdout.getvalue())
        self.assertIn("it/s", mock_stderr.getvalue())

    @mock.patch("requests.get", new=mock_get_404)
    def test_3_fetch_raises(self):
        "Does it not smoke."
        with self.assertRaises(CommandError):
            fetch_and_store(verbose=False)
