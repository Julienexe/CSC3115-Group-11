from django.db import models
from core.models import TimeStampedModel
from projects.models import Project

class Participant(TimeStampedModel):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    affiliation = models.CharField(max_length=100, choices=[
        ("cs", "Computer Science"),
        ("se", "Software Engineering"),
        ("eng", "Engineering"),
        ("other", "Other"),
    ])
    specialization = models.CharField(max_length=100, choices=[
        ("software", "Software"),
        ("hardware", "Hardware"),
        ("business", "Business"),
    ])
    cross_skill_trained = models.BooleanField(default=False)
    institution = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name




  