"""
This command stores the content of the specified filename in the database.
"""

import argparse
import os

from django.core.management.base import BaseCommand

from ...lib import import_csvz


def _check_path(value):
    path = os.path.abspath(value)
    if not os.path.exists(path):
        text = "Path '{}' does not exist ({})."
        raise argparse.ArgumentTypeError(text.format(value, path))

    return path


class Command(BaseCommand):
    "Django Command; `store`."
    help = """
    Store the specified file in the database.
    """

    def add_arguments(self, parser):
        help_text = """
        Specify the location of the compressed CSV file and add its contents to
        the DB, by default this is: '%(default)s'."""

        parser.add_argument(
            "--csv_file",
            default=import_csvz.DEFAULT_LOCATION,
            type=_check_path,
            help=help_text,
        )

    def handle(self, *args, **options):
        import_csvz.read_and_store(options["csv_file"])
