"""
Common functionality
"""
import decimal

import tqdm
from django.utils.text import slugify

from .. import models

# pylint: disable = E1101
# the no objects member of models, it really does have it though :-)


def _reset_previous_data(resource, verbose):
    "Remove previous data from that resource, if it exists and return source."
    instance, created = models.Source.objects.get_or_create(name=resource)
    if not created:
        if verbose:
            print("# - Removing previous entries.")
        instance.delete()
        if verbose:
            print("# - - Done.")

        # Recreating the resource
        instance = models.Source(name=resource)
        instance.save()

    return instance


class Bulk:
    "Store all items in the container in bulk."
    # As we use foreign keys it gets a bit tricky as we need to separate out
    # the dependencies first, this does mean we need to iterate a couple of
    # times over the container, however this is cheaper than iterating over the
    # db.
    def __init__(self, source, container, verbose):
        self.source = source
        self.container = container
        self.verbose = verbose

    def _store_delta(self, key, model):
        "Delta store values"
        # But only the ones we don't already have.
        if self.verbose:
            print("# - Storing {}s".format(key.capitalize()))

        if self.verbose:
            print("# - - Determining delta.")
            data = tqdm.tqdm(self.container)
        else:
            data = self.container

        values = {}
        for item in data:
            value = item[key]
            values[slugify(value)] = value

        existing = set(model.objects.all().values_list("slug", flat=True))
        imported = set(values.keys())

        to_store = imported.difference(existing)

        if self.verbose:
            text = "# - - Number of new {}s to be stored: {:,}"
            print(text.format(key, len(to_store)))

        bulk = []
        for slug in to_store:
            bulk.append(model(slug=slug, name=values[slug]))

        model.objects.bulk_create(bulk)

        lookup = {}
        for entry in model.objects.all().values("slug", "id"):
            lookup[entry["slug"]] = entry["id"]

        if self.verbose:
            print("# - - Done")

        return lookup

    def store_brands(self):
        "Delta store brands"
        return self._store_delta("brand", models.Brand)

    def store_retailers(self):
        "Delta store retailers"
        return self._store_delta("retailer", models.Retailer)

    def store_products(self, brands, retailers):
        "Now store the actual products"
        if self.verbose:
            print("# - Storing Products")

        bulk = []

        if self.verbose:
            print("# - - Determining Products")
            data = tqdm.tqdm(self.container)
        else:
            data = self.container

        for item in data:
            kwargs = {
                "source": self.source,
                "external_id": item["id"],
                "name": item["name"],
                "brand_id": brands[slugify(item["brand"])],
                "retailer_id": retailers[slugify(item["retailer"])],
                "in_stock": item["in_stock"],
            }

            price = item["price"]
            if price == "" or price is None:
                kwargs["price"] = None
            else:
                kwargs["price"] = decimal.Decimal(price)
            bulk.append(models.Product(**kwargs))

        if self.verbose:
            text = "# - - Number of Products to be stored: {:,}"
            print(text.format(len(bulk)))

        models.Product.objects.bulk_create(bulk)

        if self.verbose:
            print("# - - Done.")

    def store(self):
        "Store the data"
        brands = self.store_brands()
        retailers = self.store_retailers()
        self.store_products(brands, retailers)


def _sanitize_row(row, expected_keys):
    "Sanitise the row."
    tmp = {}
    # copy the row over, making sure all keys are lower and stripped, if there
    # is a value of string, strip it too and remove unnecessary quotes.
    for key, value in row.items():
        key = key.strip().lower()

        if isinstance(value, str):
            value = value.strip()
            while value.startswith('"') and value.endswith('"'):
                value = value[1:-1]

            while value.startswith("'") and value.endswith("'"):
                value = value[1:-1]

        tmp[key] = value

    # depending on the source, the key in_stock maybe instock, renaming it.
    if "instock" in tmp:
        tmp["in_stock"] = tmp.pop("instock")

    # if a key we expect is not in the row, add it with default value None.
    returned_keys = list(tmp.keys())
    returned_keys.sort()

    if expected_keys != returned_keys:
        for key in expected_keys:
            if key not in returned_keys:
                tmp[key] = None

    # `in_stock` value is a boolean which has multiple creative ways of
    # being indicated. Casting it to a real boolean or None depending.
    in_stock = tmp["in_stock"]
    if isinstance(in_stock, str):
        in_stock = in_stock.strip().lower()[0]
        if in_stock == "y":
            in_stock = True
        elif in_stock == "n":
            in_stock = False
        else:
            in_stock = None

    tmp["in_stock"] = in_stock

    return tmp


def _sanitize(data, verbose):
    "Iterate over the data and sanitise it."
    if verbose:
        print("# - Sanitizing data.")

    expected_keys = ["id", "name", "brand", "retailer", "in_stock", "price"]
    expected_keys.sort()

    container = []
    if verbose:
        data = tqdm.tqdm(data)

    for row in data:
        container.append(_sanitize_row(row, expected_keys))

    return container


def store(resource, data, verbose):
    "Store the data in the db."
    # We expect the container to be a list of dictionaries.
    if verbose:
        print("# Storing data into the DB.")

    source = _reset_previous_data(resource, verbose)
    container = _sanitize(data, verbose)

    bulk = Bulk(source, container, verbose)
    bulk.store()

    if verbose:
        print("# - Done.")
