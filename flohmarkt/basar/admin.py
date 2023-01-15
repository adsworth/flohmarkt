from datetime import date
from django.contrib import admin

from basar.models import Flohmarkt, Sale, SaleItem, Seller


class SaleItemInline(admin.TabularInline):
    """Admin Inline fpr the SaleItem model."""

    model = SaleItem
    extra = 10
    autocomplete_fields = [
        "seller",
    ]
    template = "admin/basar/sale/inline.html"


class FlohmarktAdmin(admin.ModelAdmin):
    """Model admin for Flohmarkt model."""


class SaleAdmin(admin.ModelAdmin):
    """Model admin for Sale model."""

    list_display = ("created_on", "view_gesamt_betrag")
    list_filter = ("created_by", "flohmarkt", "items__seller")
    readonly_fields = ("created_on",)

    inlines = [
        SaleItemInline,
    ]

    save_on_top = True

    def get_changeform_initial_data(self, request):
        get_data = super(SaleAdmin, self).get_changeform_initial_data(request)

        get_data["created_by"] = request.user.pk
        try:
            flohmarkt = Flohmarkt.objects.get(date_of_event=date.today())
            get_data["flohmarkt"] = flohmarkt.pk
        except (Flohmarkt.DoesNotExist, Flohmarkt.MultipleObjectsReturned):
            pass

        return get_data

    @admin.display(empty_value="???")
    def view_gesamt_betrag(self, obj: Sale):
        """Calculate the total amount for the list view"""
        total_amount = obj.gesamt_betrag()

        return f"{total_amount:.2f} €"


class SellerAdmin(admin.ModelAdmin):
    """Model admin for Seller model."""

    fields = ("flohmarkt", "number", "name", "phone", "email")
    search_fields = [
        "number",
    ]


admin.site.register(Flohmarkt, FlohmarktAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Sale, SaleAdmin)
