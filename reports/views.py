from django_tables2 import SingleTableView
from django.views.generic import ListView
from .models import Vial, Ampoule
from .tables import VialTable, AmpouleTable


class VialListView(SingleTableView):
    model = Vial
    queryset = Vial.objects.all()
    context_object_name = 'vials'
    table_class = VialTable
    template_name = 'reports/vials_list.html'


class AmpouleListView(SingleTableView):
    model = Ampoule
    queryset = Ampoule.objects.all()
    context_object_name = 'ampoules'
    table_class = AmpouleTable
    template_name = 'reports/ampoules_list.html'
