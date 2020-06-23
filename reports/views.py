from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django.views.generic import ListView
from .models import Vial, Ampoule
from .tables import VialTable, AmpouleTable, VialFilter, AmpouleFilter


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
