from django.urls import reverse
from django.db import models

from django.utils.functional import cached_property


class BaseReport(models.Model):
    """
    Base model for reports. Use this so you don't have to multiple update models
    """
    username = models.CharField(blank=False, null=False, max_length=255)
    product_id = models.IntegerField(db_index=True, blank=False, null=False)
    recipe = models.CharField(blank=False, null=False, max_length=255)
    batch_number = models.CharField(blank=True, null=True, max_length=255)
    batch_name = models.CharField(blank=True, null=True, max_length=255)
    start_date = models.DateTimeField(unique=True)
    end_date = models.DateTimeField()
    inspected = models.IntegerField(blank=False, null=False)
    accepted = models.IntegerField(blank=False, null=False)
    rejected = models.IntegerField(blank=False, null=False)
    technical_rejects = models.IntegerField(blank=False, null=False)

    audit_class = None

    class Meta:
        # Set the model to an abstract class so tables are not created for this model
        abstract = True
        
    @cached_property
    def audit_logs(self):
        return self.audit_class.objects.filter(time_stamp__range=(self.start_date, self.end_date))    
        
    @cached_property
    def safety_clutches(self):
        descriptions = [
            'ALARM SAFETY CLUTCH LOADING STARWHEEL  On',
            'ALARM SAFETY CLUTCH INTERMITTENT STARWHEEL IMPUT  On',
            'ALARM SAFETY CLUTCH INTERMITTENT STARWHEEL OUTPUT  On',
            'ALARM SAFETY CLUTCH EXIT EXTRACTING STARWHEEL FOR ACCEPTED  On',
            'ALARM SAFETY CLUTCH EXIT EXTRACTING STARWHEEL FOR REJECT  On',
        ]
        return self.audit_logs.filter(description__in=descriptions)

    def get_absolute_url(self):
        return reverse("ampoule_detail", kwargs={'pk': self.id})


class BaseAudit(models.Model):
    """
    Base model for audit logs. Use this so you don't have to multiple update models
    """
    record_id = models.IntegerField()
    time_stamp = models.DateTimeField(db_index=True)
    delta_to_utc = models.CharField(blank=True, null=True, max_length=255)
    user_id = models.CharField(blank=True, null=True, max_length=255)
    object_id = models.CharField(blank=True, null=True, max_length=255)
    description = models.CharField(blank=True, null=True, max_length=555, db_index=True)
    comment = models.CharField(blank=True, null=True, max_length=255)
    check_sum = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        # Set the model to an abstract class so tables are not created for this model
        abstract = True
        

class AmpouleAudit(BaseAudit):
    pass


class Ampoule(BaseReport):
    audit_class = AmpouleAudit


class VialAudit(BaseAudit):
    pass


class Vial(BaseReport):
    audit_class = VialAudit
