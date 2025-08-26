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


class ProjectParticipant(TimeStampedModel):
    project = models.ForeignKey(Project, related_name="project_participants", on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, related_name="participations", on_delete=models.CASCADE)
    role_on_project = models.CharField(max_length=100, choices=[
        ("student", "Student"),
        ("lecturer", "Lecturer"),
        ("contributor", "Contributor"),
    ])
    skill_role = models.CharField(max_length=100, choices=[
        ("developer", "Developer"),
        ("engineer", "Engineer"),
        ("designer", "Designer"),
        ("business_lead", "Business Lead"),
    ])

    class Meta:
        unique_together = ("project", "participant")

    def __str__(self):
        return f"{self.participant.full_name} on {self.project.title}"
