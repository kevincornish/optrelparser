from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django.views.generic import ListView
from .models import Vial, VialAudit, Ampoule, AmpouleAudit
from .tables import VialTable, VialFilter, VialAuditTable, VialAuditFilter, AmpouleTable, AmpouleFilter, AmpouleAuditTable, AmpouleAuditFilter


class VialListView(SingleTableMixin, FilterView):
    model = Vial
    queryset = Vial.objects.all()
    context_object_name = 'vials'
    table_class = VialTable
    template_name = 'reports/vials_list.html'
    filterset_class = VialFilter


class AmpouleListView(SingleTableMixin, FilterView):
    model = Ampoule
    queryset = Ampoule.objects.all()
    context_object_name = 'ampoules'
    table_class = AmpouleTable
    template_name = 'reports/ampoules_list.html'
    filterset_class = AmpouleFilter
    
class VialAuditListView(SingleTableMixin, FilterView):
    model = VialAudit
    queryset = VialAudit.objects.all()
    context_object_name = 'vialaudit'
    table_class = VialAuditTable
    template_name = 'reports/vial_audit_list.html'
    filterset_class = VialAuditFilter


class AmpouleAuditListView(SingleTableMixin, FilterView):
    model = AmpouleAudit
    queryset = AmpouleAudit.objects.all()
    context_object_name = 'ampouleaudit'
    table_class = AmpouleAuditTable
    template_name = 'reports/ampoule_audit_list.html'
    filterset_class = AmpouleAuditFilter

