"""
This command fetches a CSV from the specified source and pipes the output to
standard out.
"""

from django.core.management.base import BaseCommand

from ...lib import import_json


class Command(BaseCommand):
    "Django Command; `fetch`."
    help = """
    Download a CSV from the specified location and outputs the content to
    standard out.
    """

    def add_arguments(self, parser):
        help_text = """
        Specify location from where to download the JSON, by default this
        is: '%(default)s'."""

        parser.add_argument(
            "--url", type=str, default=import_json.DEFAULT_LOCATION, help=help_text
        )

    def handle(self, *args, **options):
        import_json.fetch_and_store(options["url"])
