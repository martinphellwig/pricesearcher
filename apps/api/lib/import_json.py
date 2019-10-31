"""
This module contains the fetch function which is used in the django command
fetch function.
"""
import requests
from django.core.management.base import CommandError

from .import_store import store

DEFAULT_LOCATION = (
    "https://s3-eu-west-1.amazonaws.com/"
    "pricesearcher-code-tests/python-software-developer/products.json"
)


def fetch_and_store(url=DEFAULT_LOCATION, verbose=True):
    "Fetch JSON from url and store it in the DB."
    response = None
    resource_name = url.rsplit("/", 1)[1]

    if verbose:
        print("# Fetching data from: {}".format(url))

    response = requests.get(url)
    if response.status_code != 200:
        error_text = "Status code '{}' raised for url '{}'.".format(
            response.status_code, url
        )
        raise CommandError(error_text)

    json_data = response.json()

    if verbose:
        print("# - Done")

    store(resource_name, json_data, verbose)
