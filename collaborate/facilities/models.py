from django.db import models
from core.models import TimeStampedModel

class Facility(TimeStampedModel):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    partner_organization = models.CharField(max_length=255, blank=True, null=True)
    facility_type = models.CharField(max_length=100, choices=[
        ("lab", "Lab"),
        ("workshop", "Workshop"),
        ("testing", "Testing Center"),
    ])
    capabilities = models.TextField(help_text="e.g., CNC, PCB fabrication, materials testing")

    def __str__(self):
        return self.name


class Service(TimeStampedModel):
    facility = models.ForeignKey(Facility, related_name="services", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ("machining", "Machining"),
        ("testing", "Testing"),
        ("training", "Training"),
    ])
    skill_type = models.CharField(max_length=100, choices=[
        ("hardware", "Hardware"),
        ("software", "Software"),
        ("integration", "Integration"),
    ])

    def __str__(self):
        return f"{self.name} ({self.facility.name})"


class Equipment(TimeStampedModel):
    facility = models.ForeignKey(Facility, related_name="equipment", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    capabilities = models.TextField()
    description = models.TextField()
    inventory_code = models.CharField(max_length=100, unique=True)
    usage_domain = models.CharField(max_length=100, help_text="Electronics, Mechanical, IoT")
    support_phase = models.CharField(max_length=100, help_text="Training, Prototyping, Testing, Commercialization")

    def __str__(self):
        return f"{self.name} - {self.facility.name}"
