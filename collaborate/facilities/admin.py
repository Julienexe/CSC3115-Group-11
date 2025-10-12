from django.contrib import admin
from .models import Facility, Service, Equipment

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "facility_type", "partner_organization")
    search_fields = ("name", "location", "partner_organization")
    list_filter = ("facility_type",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "facility", "category", "skill_type")
    search_fields = ("name", "category", "skill_type")
    list_filter = ("category", "skill_type")

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "facility", "inventory_code", "usage_domain", "support_phase")
    search_fields = ("name", "inventory_code", "usage_domain")
    list_filter = ("usage_domain", "support_phase")