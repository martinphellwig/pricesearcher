# pylint: disable=C0103
"""
Initial migration.
"""

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Django generated migration file.
    """

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=64, null=True)),
                (
                    "slug",
                    models.SlugField(blank=True, max_length=64, null=True, unique=True),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Retailer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=64, null=True)),
                (
                    "slug",
                    models.SlugField(blank=True, max_length=64, null=True, unique=True),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("external_id", models.CharField(max_length=16)),
                ("name", models.CharField(blank=True, max_length=64, null=True)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, max_digits=8, null=True),
                ),
                ("in_stock", models.BooleanField(null=True)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.Brand"
                    ),
                ),
                (
                    "retailer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.Retailer"
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.Source"
                    ),
                ),
            ],
            options={"unique_together": {("external_id", "name", "brand", "retailer")}},
        ),
    ]
