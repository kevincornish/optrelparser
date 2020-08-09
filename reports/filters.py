import django_filters
from .models import Ampoule, AmpouleAudit, Vial, VialAudit

class VialFilter(django_filters.FilterSet):
    class Meta:
        model = Vial
        fields = {
            'username': ['iexact'],
            'recipe': ['icontains'],
            'batch_number': ['exact'],
            'batch_name': ['icontains'],
        }


class AmpouleFilter(django_filters.FilterSet):
    class Meta:
        model = Ampoule
        fields = {
            'username': ['iexact'],
            'recipe': ['icontains'],
            'batch_number': ['exact'],
            'batch_name': ['icontains'],
        }
        
        
class VialAuditFilter(django_filters.FilterSet):
    class Meta:
        model = VialAudit
        fields = {
            'user_id': ['icontains'],
            'description': ['icontains'],
        }


class AmpouleAuditFilter(django_filters.FilterSet):
    class Meta:
        model = AmpouleAudit
        fields = {
            'user_id': ['icontains'],
            'description': ['icontains'],
        }