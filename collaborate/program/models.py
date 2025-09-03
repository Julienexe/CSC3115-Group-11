from django.db import models
from core.models import TimeStampedModel

class Program(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    national_alignment = models.CharField(max_length=255, help_text="Link to NDPIII, Roadmap, or 4IR goals")
    focus_areas = models.CharField(max_length=255, help_text="Domains such as IoT, automation, renewable energy")
    phases = models.CharField(max_length=255, help_text="Cross-Skilling, Collaboration, etc.")

    def __str__(self):
        return self.name
