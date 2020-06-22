from django.views.generic import ListView
from .models import Vial


class VialListView(ListView):
    model = Vial
    queryset = Vial.objects.all()
    context_object_name = 'vials'
    template_name = 'reports/vials_list.html'