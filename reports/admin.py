from django.contrib import admin

from . import models


@admin.register(models.Vial)
class ReportModelAdmin(admin.ModelAdmin):
    list_display = ("username", "product_id", "recipe", "batch_number", "batch_name")
