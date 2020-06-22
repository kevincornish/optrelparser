from django.views.generic import ListView
from .models import Vial


class VialListView(ListView):
    # You can customize things in this class like pagination and ordering and such very easily.
    # Check the link, this resource is key for django.
    # http://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/
    # Don't forget to register your view in optrel/urls.py
    model = Vial
    queryset = Vial.objects.all()
    context_object_name = 'vials'
    template_name = 'reports/vials_list.html'