"""
This module contains the store function which is used in the django command
store function.
"""
import csv
import gzip
import io
import os

from django.conf import settings

from .import_store import store

DEFAULT_LOCATION = os.path.join(
    settings.BASE_DIR, "_project", "resources", "products.csv.gz"
)


def read_and_store(filename=DEFAULT_LOCATION, verbose=True):
    "Store the contents of the file in the DB."
    resource_name = os.path.split(filename)[1]
    if verbose:
        print("# Reading file: {}".format(resource_name))

    # We technically don't need to convert the data to an io type, however
    # csv sort of expects it, however the principal of doing things the
    # obvious way stands, and I am Dutch so I sort of stand on it :-)
    gzip_data = io.StringIO()
    with gzip.open(filename, "rt") as gzip_open:
        gzip_data.write(gzip_open.read())

    gzip_data.seek(0)
    csv_data = list(csv.DictReader(gzip_data))

    if verbose:
        print("# - Done")

    store(resource_name, csv_data, verbose)
