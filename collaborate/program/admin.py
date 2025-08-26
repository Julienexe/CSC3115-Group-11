from django.contrib import admin
from .models import Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "national_alignment", "created_at")
    search_fields = ("name", "focus_areas", "phases")
    list_filter = ("national_alignment",)
