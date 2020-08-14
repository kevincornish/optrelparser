from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django.views.generic import DetailView
from django.shortcuts import render
from django.http import Http404
from django.db.models import Count

from .models import Ampoule, AmpouleAudit, Vial, VialAudit
from .tables import AmpouleAuditTable, AmpouleTable, VialAuditTable, VialTable
from .filters import AmpouleAuditFilter, AmpouleFilter, VialAuditFilter, VialFilter

def Dashboard(request):
    current_user_groups = request.user.groups.values_list("name", flat=True)
    context = {
        "is_supervisor": "Supervisor" in current_user_groups,
        "is_senior_operator": "Senior Operator" in current_user_groups,
    }

    return render(request, "reports/dashboard.html", context)


class VialListView(SingleTableMixin, FilterView):
    model = Vial
    queryset = Vial.objects.all()
    context_object_name = 'vials'
    table_class = VialTable
    template_name = 'reports/vials_list.html'
    filterset_class = VialFilter


class VialDetailView(SingleTableMixin, DetailView):
    table_class = VialAuditTable
    model = VialAudit
    queryset = VialAudit.objects.all()
    context_object_name = 'audit_logs'
    template_name = 'reports/vials_detail.html'
    paginate_by = 25

    def get_object(self, queryset=None):
        try:
            obj = Vial.objects.get(pk=self.kwargs.get(self.pk_url_kwarg))
        except Vial.DoesNotExist:
            raise Http404("Vial does not exist")
        if not hasattr(self, 'object'):
            self.object = obj
        return obj

    def get_context_data(self, **kwargs):
        obj = self.get_object()
        data = super().get_context_data(**kwargs)
        batch_pk = self.kwargs.get('pk', None)
        f = VialAuditFilter(self.request.GET, queryset=VialAudit.objects.filter(id=batch_pk))
        clutches = ( 
            self.object.safety_clutches.values('description').order_by('description')
            .annotate(count=Count('description'))
        )
        data.update({
            'clutches': clutches,
            'filter': f,
            'vial': obj
        })
        return data

    def get_queryset(self):
        obj = self.get_object()
        return obj.audit_logs

class VialPrintView(VialDetailView):
    template_name = 'reports/vials_print.html'
    paginate_by = 2500
    pass

class VialAuditListView(SingleTableMixin, FilterView):
    model = VialAudit
    queryset = VialAudit.objects.all()
    context_object_name = 'vialaudit'
    table_class = VialAuditTable
    template_name = 'reports/vial_audit_list.html'
    filterset_class = VialAuditFilter

class AmpouleListView(SingleTableMixin, FilterView):
    model = Ampoule
    queryset = Ampoule.objects.all()
    context_object_name = 'ampoules'
    table_class = AmpouleTable
    template_name = 'reports/ampoules_list.html'
    filterset_class = AmpouleFilter


class AmpouleDetailView(SingleTableMixin, DetailView):
    table_class = AmpouleAuditTable
    model = AmpouleAudit
    queryset = AmpouleAudit.objects.all()
    context_object_name = 'audit_logs'
    template_name = 'reports/ampoules_detail.html'
    def get_object(self, queryset=None):
        try:
            obj = Ampoule.objects.get(pk=self.kwargs.get(self.pk_url_kwarg))
        except Ampoule.DoesNotExist:
            raise Http404("Ampoule does not exist")    
        if not hasattr(self, 'object'):
            self.object = obj
        return obj

    def get_context_data(self, **kwargs):
        obj = self.get_object()
        data = super().get_context_data(**kwargs)
        batch_pk = self.kwargs.get('pk', None)
        f = AmpouleAuditFilter(self.request.GET, queryset=AmpouleAudit.objects.filter(id=batch_pk))
        clutches = ( 
            self.object.safety_clutches.values('description').order_by('description')
            .annotate(count=Count('description'))
        )
        data.update({
            'clutches': clutches,
            'filter': f,
            'ampoule': obj
        })
        return data

    def get_queryset(self):
        obj = self.get_object()
        return obj.audit_logs

class AmpoulePrintView(AmpouleDetailView):
    template_name = 'reports/ampoules_print.html'
    paginate_by = 2500
    pass

class AmpouleAuditListView(SingleTableMixin, FilterView):
    model = AmpouleAudit
    queryset = AmpouleAudit.objects.all()
    context_object_name = 'ampouleaudit'
    table_class = AmpouleAuditTable
    template_name = 'reports/ampoule_audit_list.html'
    filterset_class = AmpouleAuditFilter
