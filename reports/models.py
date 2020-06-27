from django.db import models


class BaseReport(models.Model):
    """
    Base model for reports. Use this so you don't have to multiple update models
    """
    username = models.CharField(blank=False, null=False, max_length=255)
    product_id = models.IntegerField(db_index=True, blank=False, null=False)
    recipe = models.CharField(blank=False, null=False, max_length=255)
    batch_number = models.IntegerField(blank=True, null=True)
    batch_name = models.CharField(blank=True, null=True, max_length=255)
    start_date = models.DateTimeField(primary_key=True)
    end_date = models.DateTimeField()
    inspected = models.IntegerField(blank=False, null=False)
    accepted = models.IntegerField(blank=False, null=False)
    rejected = models.IntegerField(blank=False, null=False)
    technical_rejects = models.IntegerField(blank=False, null=False)

    class Meta:
        # Set the model to an abstract class so tables are not created for this model
        abstract = True


class BaseAudit(models.Model):
    """
    Base model for audit logs. Use this so you don't have to multiple update models
    """
    record_id = models.IntegerField()
    time_stamp = models.DateTimeField(db_index=True)
    delta_to_utc = models.CharField(blank=True, null=True, max_length=255)
    user_id = models.CharField(blank=True, null=True, max_length=255)
    object_id = models.CharField(blank=True, null=True, max_length=255)
    description = models.CharField(blank=True, null=True, max_length=555)
    comment = models.CharField(blank=True, null=True, max_length=255)
    check_sum = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        # Set the model to an abstract class so tables are not created for this model
        abstract = True


class Ampoule(BaseReport):
    pass


class AmpouleAudit(BaseAudit):
    pass


class Vial(BaseReport):
    pass


class VialAudit(BaseAudit):
    pass
