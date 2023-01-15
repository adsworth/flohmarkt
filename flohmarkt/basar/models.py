from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Flohmarkt(models.Model):
    """Flohmarkt Event"""

    name = models.CharField(primary_key=True, null=False, max_length=200)
    date_of_event = models.DateField(null=False)

    class Meta:
        """Meta class for model Flohmarkt"""

        verbose_name = "Flohmarkt"
        verbose_name_plural = "Flohmärkte"

    def __str__(self) -> str:
        return f"{self.name} am {self.date_of_event:%d.%m.%Y }"


class Seller(models.Model):
    """Anbieter/Verkäufer"""

    number = models.IntegerField(null=False, unique=True, verbose_name="Nummer")
    name = models.CharField(null=False, max_length=200, verbose_name="Name")
    phone = models.CharField(
        blank=True, default="", max_length=200, verbose_name="Telefonnummer"
    )
    email = models.CharField(
        blank=True, default="", max_length=200, verbose_name="Emailadresse"
    )

    flohmarkt = models.ForeignKey(
        Flohmarkt, on_delete=models.CASCADE, related_name="seller"
    )

    class Meta:
        """Meta class for model Seller"""

        ordering = ["number"]
        verbose_name = "Anbieter"
        verbose_name_plural = "Anbieter"

    def __str__(self) -> str:
        return f"Anbieter {self.number}: {self.name}"


class Sale(models.Model):
    """Ein Verkauf"""

    created_on = models.DateTimeField(
        default=timezone.now, verbose_name="Verkaufszeitpunkt"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    flohmarkt = models.ForeignKey(Flohmarkt, on_delete=models.CASCADE)

    class Meta:
        """Meta class for model Sale"""

        ordering = ["-created_on"]
        verbose_name = "Verkauf"
        verbose_name_plural = "Verkäufe"

    def __str__(self) -> str:
        return f"Verkauf um {self.created_on:%d.%m.%Y %H:%m:%S}"

    def gesamt_betrag(self):
        """returns the total sale amount."""
        aggregated = self.items.aggregate(total_amount=models.Sum("amount"))
        return aggregated["total_amount"]


class SaleItem(models.Model):
    """Ein verkaufter Gegenstand eines Anbieters"""

    seller = models.ForeignKey(
        Seller, null=False, on_delete=models.CASCADE, verbose_name="Anbieter"
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, verbose_name="Betrag"
    )
    sale = models.ForeignKey(
        Sale,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Verkauf",
        related_name="items",
    )

    class Meta:
        """Meta class for model SaleItem"""

        verbose_name = "Verkaufsobjekt"
        verbose_name_plural = "Verkaufsobjekte"
