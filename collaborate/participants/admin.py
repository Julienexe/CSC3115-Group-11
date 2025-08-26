from django.contrib import admin
from .models import Participant, ProjectParticipant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "affiliation", "specialization", "institution")
    search_fields = ("full_name", "email", "institution")
    list_filter = ("affiliation", "specialization", "cross_skill_trained")

@admin.register(ProjectParticipant)
class ProjectParticipantAdmin(admin.ModelAdmin):
    list_display = ("participant", "project", "role_on_project", "skill_role")
    search_fields = ("participant__full_name", "project__title")
    list_filter = ("role_on_project", "skill_role")
