"""
Test Cases for appconfig
"""
from unittest import mock

from django.test import TestCase

from ..apps import _ready

MOCK_JSON = "apps.api.lib.import_json.fetch_and_store"


class TestAppConfig(TestCase):
    "Test cases for app config ready"

    @mock.patch.dict("os.environ", {"RUN_MAIN": "false"})
    def test_1_ready_not_called(self):
        "Does it return a string."
        self.assertFalse(_ready())

    @mock.patch.dict("os.environ", {"RUN_MAIN": "true"})
    @mock.patch(MOCK_JSON, mock.MagicMock(return_value=None))
    def test_2_ready_called(self):
        "Does it return a string."
        self.assertTrue(_ready())
