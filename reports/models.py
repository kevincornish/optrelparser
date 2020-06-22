from django.db import models


class Vial(models.Model):
    username = models.CharField(blank=False, null=False, max_length=255)
    product_id = models.IntegerField(db_index=True, blank=False, null=False)
    recipe = models.CharField(blank=False, null=False, max_length=255)
    batch_number = models.IntegerField(blank=True, null=True)
    batch_name = models.CharField(blank=True, null=True, max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    inspected = models.IntegerField(blank=False, null=False)
    accepted = models.IntegerField(blank=False, null=False)
    rejected = models.IntegerField(blank=False, null=False)
    technical_rejects = models.IntegerField(blank=False, null=False)

class Ampoule(models.Model):
    username = models.CharField(blank=False, null=False, max_length=255)
    product_id = models.IntegerField(db_index=True, blank=False, null=False)
    recipe = models.CharField(blank=False, null=False, max_length=255)
    batch_number = models.IntegerField(blank=True, null=True)
    batch_name = models.CharField(blank=True, null=True, max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    inspected = models.IntegerField(blank=False, null=False)
    accepted = models.IntegerField(blank=False, null=False)
    rejected = models.IntegerField(blank=False, null=False)
    technical_rejects = models.IntegerField(blank=False, null=False)
