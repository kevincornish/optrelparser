import django_tables2 as tables
import django_filters
from django_tables2.utils import A

from .models import Ampoule, AmpouleAudit, Vial, VialAudit


class VialTable(tables.Table):
    id = tables.Column(linkify=("vial_detail", [tables.A("id")]))
    start_date = tables.DateTimeColumn(format ='d/m/Y, g:i a')
    end_date = tables.DateTimeColumn(format ='d/m/Y, g:i a')

    class Meta:
        order_by = "-start_date"
        model = Vial
        template_name = "django_tables2/bootstrap.html"
        fields = (
            "id", "batch_number", "batch_name", "recipe", "start_date", "end_date", "username", "inspected",
            "accepted", "rejected", "technical_rejects")
        row_attrs = {
            'recipe': lambda record: record.recipe
        }
        
        
class AmpouleTable(tables.Table):
    id = tables.LinkColumn("ampoule_detail", args=[A("pk")])
    start_date = tables.DateTimeColumn(format ='d/m/Y, g:i a')
    end_date = tables.DateTimeColumn(format ='d/m/Y, g:i a')
    
    class Meta:
        order_by="-start_date"
        model = Ampoule
        template_name = "django_tables2/bootstrap.html"
        fields = (
            "id", "batch_number", "batch_name", "recipe", "start_date", "end_date", "username", "inspected",
            "accepted", "rejected", "technical_rejects")
        row_attrs = {
            'recipe': lambda record: record.recipe
        }


class VialAuditTable(tables.Table):
    time_stamp = tables.DateTimeColumn(format ='d/m/Y, g:i a')
    class Meta:
        order_by = "time_stamp"
        model = VialAudit
        template_name = "django_tables2/bootstrap.html"
        fields = ("time_stamp", "user_id", "object_id", "description")
        row_attrs = {
            'object_id': lambda record: record.object_id
        }

class AmpouleAuditTable(tables.Table):
    time_stamp = tables.DateTimeColumn(format ='d/m/Y, g:i a')
    class Meta:
        order_by = "time_stamp"
        model = AmpouleAudit
        template_name = "django_tables2/bootstrap.html"
        fields = ("time_stamp", "user_id", "object_id", "description")
        row_attrs = {
            'object_id': lambda record: record.object_id
        }