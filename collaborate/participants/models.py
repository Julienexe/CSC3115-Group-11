from django.db import models
from core.models import TimeStampedModel
from django.forms import ValidationError
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

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_participant_email')
        ]

    def __str__(self):
        return self.full_name
    
    def clean(self):
        if self.pk:
            if not self.full_name or not self.email or not self.affiliation:
                raise ValidationError(
                    "Participant.FullName, Participant.Email, and Participant.Affiliation are required."
                )
            
            if self.cross_skill_trained and not self.specialization:
                raise ValidationError(
                    "Cross-skill flag requires Specialization."
                )