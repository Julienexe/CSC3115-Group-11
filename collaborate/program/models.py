# apps/capstone/models.py
from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Program(TimeStampedModel):
    # 1.1.1 Program fields (simplified but aligned to spec) :contentReference[oaicite:1]{index=1}
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    national_alignment = models.CharField(max_length=255, blank=True)  # NDPIII, Roadmap, 4IR
    focus_areas = models.CharField(max_length=255, blank=True)         # e.g., "IoT, automation"
    phases = models.CharField(max_length=255, blank=True)              # e.g., "Cross-Skilling,..."

    def __str__(self):
        return self.name


class Project(TimeStampedModel):
    # 1.1.5 Project fields (subset needed for these use cases) :contentReference[oaicite:2]{index=2}
    NATURE_CHOICES = [
        ("research", "Research"),
        ("prototype", "Prototype"),
        ("applied", "Applied Work"),
    ]
    PROTOTYPE_STAGE_CHOICES = [
        ("concept", "Concept"),
        ("prototype", "Prototype"),
        ("mvp", "MVP"),
        ("launch", "Market Launch"),
    ]

    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    nature_of_project = models.CharField(max_length=20, choices=NATURE_CHOICES, default="prototype")
    description = models.TextField(blank=True)
    innovation_focus = models.CharField(max_length=255, blank=True)    # e.g., IoT devices, renewable energy
    prototype_stage = models.CharField(max_length=20, choices=PROTOTYPE_STAGE_CHOICES, default="concept")
    testing_requirements = models.TextField(blank=True)
    commercialization_plan = models.TextField(blank=True)

    def __str__(self):
        return self.title


def outcome_artifact_upload_to(instance, filename):
    # stored as: outcomes/<project_id>/<filename>
    return f"outcomes/{instance.project_id}/{filename}"


class Outcome(TimeStampedModel):
    # 1.1.8 Outcome fields (with upload support) :contentReference[oaicite:3]{index=3}
    OUTCOME_TYPE_CHOICES = [
        ("cad", "CAD"),
        ("pcb", "PCB"),
        ("prototype", "Prototype"),
        ("report", "Report"),
        ("business_plan", "Business Plan"),
    ]
    COMMERCIALIZATION_STATUS_CHOICES = [
        ("demoed", "Demoed"),
        ("market_linked", "Market Linked"),
        ("launched", "Launched"),
        ("na", "Not Applicable"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="outcomes")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # Either upload a file OR store a URL link (both optional but at least one required via serializer validation)
    artifact_file = models.FileField(upload_to=outcome_artifact_upload_to, blank=True, null=True)
    artifact_link = models.URLField(blank=True)
    outcome_type = models.CharField(max_length=20, choices=OUTCOME_TYPE_CHOICES)
    quality_certification = models.CharField(max_length=255, blank=True)  # e.g., UIRI certification
    commercialization_status = models.CharField(
        max_length=20, choices=COMMERCIALIZATION_STATUS_CHOICES, default="na"
    )

    def __str__(self):
        return f"{self.title} (Project #{self.project_id})"
