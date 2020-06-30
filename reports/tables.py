import django_tables2 as tables
import django_filters
from django_tables2.utils import A

from .models import Ampoule, AmpouleAudit, Vial, VialAudit


class VialTable(tables.Table):
    class Meta:
        model = Vial
        template_name = "django_tables2/bootstrap.html"
        fields = (
            "username", "product_id", "recipe", "batch_number", "batch_name", "start_date", "end_date", "inspected",
            "accepted", "rejected", "technical_rejects")


class AmpouleTable(tables.Table):
    id = tables.LinkColumn("ampoule_detail", args=[A("pk")])

    class Meta:
        model = Ampoule
        template_name = "django_tables2/bootstrap.html"
        fields = (
            "id", "username", "product_id", "recipe", "batch_number", "batch_name", "start_date", "end_date", "inspected",
            "accepted", "rejected", "technical_rejects")


class VialFilter(django_filters.FilterSet):
    class Meta:
        model = Vial
        fields = ["username", "product_id", "recipe", "batch_number", "batch_name"]


class AmpouleFilter(django_filters.FilterSet):
    class Meta:
        model = Ampoule
        fields = ["username", "product_id", "recipe", "batch_number", "batch_name"]


class VialAuditTable(tables.Table):
    class Meta:
        model = VialAudit
        template_name = "django_tables2/bootstrap.html"
        fields = ("time_stamp", "user_id", "object_id", "description")


class AmpouleAuditTable(tables.Table):
    class Meta:
        model = AmpouleAudit
        template_name = "django_tables2/bootstrap.html"
        fields = ("time_stamp", "user_id", "object_id", "description")


class VialAuditFilter(django_filters.FilterSet):
    class Meta:
        model = VialAudit
        fields = ["time_stamp", "user_id", "object_id", "description"]


class AmpouleAuditFilter(django_filters.FilterSet):
    class Meta:
        model = AmpouleAudit
        fields = ["time_stamp", "user_id", "object_id", "description"]
