from django.contrib import admin
from .models import Project, Outcome

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "program", "facility", "nature_of_project", "prototype_stage")
    search_fields = ("title", "innovation_focus", "description")
    list_filter = ("nature_of_project", "prototype_stage", "program", "facility")

@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "outcome_type", "commercialization_status")
    search_fields = ("title", "description", "outcome_type")
    list_filter = ("outcome_type", "commercialization_status")
