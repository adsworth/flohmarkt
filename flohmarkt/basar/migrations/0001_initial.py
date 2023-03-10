# Generated by Django 4.1.5 on 2023-01-15 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Flohmarkt",
            fields=[
                (
                    "name",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("date_of_event", models.DateField()),
            ],
            options={
                "verbose_name": "Flohmarkt",
                "verbose_name_plural": "Flohmärkte",
            },
        ),
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Verkaufszeitpunkt",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "flohmarkt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="basar.flohmarkt",
                    ),
                ),
            ],
            options={
                "verbose_name": "Verkauf",
                "verbose_name_plural": "Verkäufe",
                "ordering": ["-created_on"],
            },
        ),
        migrations.CreateModel(
            name="Seller",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField(unique=True, verbose_name="Nummer")),
                ("name", models.CharField(max_length=200, verbose_name="Name")),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=200,
                        verbose_name="Telefonnummer",
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=200,
                        verbose_name="Emailadresse",
                    ),
                ),
                (
                    "flohmarkt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seller",
                        to="basar.flohmarkt",
                    ),
                ),
            ],
            options={
                "verbose_name": "Anbieter",
                "verbose_name_plural": "Anbieter",
                "ordering": ["number"],
            },
        ),
        migrations.CreateModel(
            name="SaleItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Betrag"
                    ),
                ),
                (
                    "sale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="basar.sale",
                        verbose_name="Verkauf",
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="basar.seller",
                        verbose_name="Anbieter",
                    ),
                ),
            ],
            options={
                "verbose_name": "Verkaufsobjekt",
                "verbose_name_plural": "Verkaufsobjekte",
            },
        ),
    ]
