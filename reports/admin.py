from django.contrib import admin

from . import models


@admin.register(models.Vial)
class VialModelAdmin(admin.ModelAdmin):
    list_display = ("username", "product_id", "recipe", "batch_number", "batch_name")


@admin.register(models.VialAudit)
class VialAuditModelAdmin(admin.ModelAdmin):
    list_display = ("record_id", "user_id", "description", "comment")


@admin.register(models.Ampoule)
class AmpouleModelAdmin(admin.ModelAdmin):
    list_display = ("username", "product_id", "recipe", "batch_number", "batch_name")


@admin.register(models.AmpouleAudit)
class AmpouleAuditModelAdmin(admin.ModelAdmin):
    list_display = ("record_id", "user_id", "description", "comment")
