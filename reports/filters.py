import django_filters
from .models import Ampoule, AmpouleAudit, Vial, VialAudit

class VialFilter(django_filters.FilterSet):
    class Meta:
        model = Vial
        fields = {
            'username': ['exact'],
            'recipe': ['contains'],
            'batch_number': ['exact'],
            'batch_name': ['contains'],
        }


class AmpouleFilter(django_filters.FilterSet):
    class Meta:
        model = Ampoule
        fields = {
            'username': ['exact'],
            'recipe': ['contains'],
            'batch_number': ['exact'],
            'batch_name': ['contains'],
        }
        
        
class VialAuditFilter(django_filters.FilterSet):
    class Meta:
        model = VialAudit
        fields = ["time_stamp", "user_id", "object_id", "description"]


class AmpouleAuditFilter(django_filters.FilterSet):
    class Meta:
        model = AmpouleAudit
        fields = ["time_stamp", "user_id", "object_id", "description"]
