"""
Test Cases for csvz import
"""
import io
from contextlib import contextmanager
from unittest import mock

from django.test import TestCase

from ..lib.import_csvz import read_and_store


@contextmanager
def _mock_gzip_open(filename, mode):
    "Simple mocked gzip open"
    assert filename
    assert mode
    yield io.StringIO("this, is, a, test")


MOCK_STORE = "apps.api.lib.import_store.store"

# pylint: disable=R0201
# Did not use any 'self' in the tests, blame unittest for that ;-)
class TestCommand(TestCase):
    "Test cases for import csvz"

    @mock.patch("gzip.open", new=_mock_gzip_open)
    def test_1_read_and_store_quite(self):
        "Does it not smoke."
        read_and_store(verbose=False)

    @mock.patch("gzip.open", new=_mock_gzip_open)
    @mock.patch("sys.stdout", new_callable=io.StringIO)
    @mock.patch("sys.stderr", new_callable=io.StringIO)
    def test_2_read_and_store_verbose(self, mock_stderr, mock_stdout):
        "Does it not smoke."
        read_and_store()
        self.assertIn("Done", mock_stdout.getvalue())
        self.assertIn("it/s", mock_stderr.getvalue())
