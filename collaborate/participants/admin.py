from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "affiliation", "specialization", "institution")
    search_fields = ("full_name", "email", "institution")
    list_filter = ("affiliation", "specialization", "cross_skill_trained")

