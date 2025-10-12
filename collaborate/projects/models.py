from django.db import models
from django.forms import ValidationError
from core.models import TimeStampedModel
from programs.models import Program
from facilities.models import Facility

class Project(TimeStampedModel):
    program = models.ForeignKey(Program, related_name="projects", on_delete=models.PROTECT)
    facility = models.ForeignKey(Facility, related_name="projects", on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    nature_of_project = models.CharField(max_length=100, choices=[
        ("research", "Research"),
        ("prototype", "Prototype"),
        ("applied", "Applied Work"),
    ])
    description = models.TextField()
    innovation_focus = models.CharField(max_length=255, help_text="IoT devices, smart home, renewable energy")
    prototype_stage = models.CharField(max_length=100, choices=[
        ("concept", "Concept"),
        ("prototype", "Prototype"),
        ("mvp", "MVP"),
        ("launch", "Market Launch"),
    ])
    status = models.CharField(max_length=100, choices=[
        ("completed", "Completed"),
        ("in_progress", "In Progress"),
        ("on_hold", "On Hold"),
        ("cancelled", "Cancelled"),], default="in_progress")
    testing_requirements = models.TextField(blank=True, null=True)
    commercialization_plan = models.TextField(blank=True, null=True)

    class Meta:
        constraints = [
           
            models.UniqueConstraint(fields=['program', 'title'], name='unique_project_title_per_program')
        ]

    def __str__(self):
        return self.title
    
    def clean(self):
        super().clean()
        if not self.program_id and not self.facility_id:
            raise ValidationError("Project.ProgramId and Project.FacilityId are required.")
        
        if self.status == "completed" and not self.outcomes.exists():
            raise ValidationError("Completed projects must have at least one documented outcome.")

class Outcome(TimeStampedModel):
    project = models.ForeignKey(Project, related_name="outcomes", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    artifact_link = models.URLField(blank=True, null=True)
    outcome_type = models.CharField(max_length=100, choices=[
        ("cad", "CAD"),
        ("pcb", "PCB"),
        ("prototype", "Prototype"),
        ("report", "Report"),
        ("business_plan", "Business Plan"),
    ])
    quality_certification = models.CharField(max_length=255, blank=True, null=True)
    commercialization_status = models.CharField(max_length=100, choices=[
        ("demoed", "Demoed"),
        ("market_linked", "Market Linked"),
        ("launched", "Launched"),
    ], blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.project.title})"
