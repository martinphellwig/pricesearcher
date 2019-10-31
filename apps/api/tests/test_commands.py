"""
Test Cases for Commands
Just making sure they don't cause any errors when executing.
"""
import argparse
from unittest import mock

from django.core.management import call_command
from django.test import TestCase

from ..management.commands.import_csvz import _check_path

MOCK_JSON = "apps.api.lib.import_json.fetch_and_store"
MOCK_CSVZ = "apps.api.lib.import_csvz.read_and_store"

# pylint: disable=R0201
# Did not use any 'self' in the tests, blame unittest for that ;-)
class TestCommand(TestCase):
    "Test cases for commands"

    @mock.patch(MOCK_JSON, mock.MagicMock(return_value=None))
    def test_1_cmd_import_json(self):
        "Does it not smoke."
        call_command("import_json")

    @mock.patch(MOCK_CSVZ, mock.MagicMock(return_value=None))
    def test_2_cmd_import_csvz(self):
        "Does it not smoke."
        call_command("import_csvz")

    def test_3_check_path(self):
        "Check if the checkpath throws an error."
        with self.assertRaises(argparse.ArgumentTypeError):
            _check_path("!invalid!")
