import django_tables2 as tables
from .models import Vial, Ampoule

class VialTable(tables.Table):
    class Meta:
        model = Vial
        template_name = "django_tables2/bootstrap.html"
        fields = ("username", "product_id", "recipe", "batch_number", "batch_name", "start_date", "end_date", "inspected", "accepted", "rejected", "technical_rejects")

class AmpouleTable(tables.Table):
    class Meta:
        model = Ampoule
        template_name = "django_tables2/bootstrap.html"
        fields = ("username", "product_id", "recipe", "batch_number", "batch_name", "start_date", "end_date", "inspected", "accepted", "rejected", "technical_rejects")
