# apps/capstone/admin.py
from django.contrib import admin
from .models import Program, Project, Outcome

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "national_alignment", "created_at")
    search_fields = ("name", "national_alignment", "focus_areas", "phases")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "program", "prototype_stage", "created_at")
    list_filter = ("program", "prototype_stage", "nature_of_project")
    search_fields = ("title", "innovation_focus")

@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "outcome_type", "commercialization_status", "created_at")
    list_filter = ("outcome_type", "commercialization_status")
    search_fields = ("title", "quality_certification")
