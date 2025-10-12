from django.db import models
from core.models import TimeStampedModel
from django.forms import ValidationError

class Program(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    national_alignment = models.CharField(max_length=255, blank=True)
    focus_areas = models.CharField(max_length=255, blank=True)
    phases = models.CharField(max_length=255, blank=True)

    class Meta:
        constraints = [
            # if focus ares is unset, national alignment must be set
            models.CheckConstraint(
                check=(
                    models.Q(focus_areas__isnull=False) | models.Q(national_alignment__isnull=True)
                ),
                name='focus_areas_requires_national_alignment'
            ),
            models.UniqueConstraint(fields=['name'], name='unique_program_name')
        ]

    def _delete_guard(self):
        if self.projects.exists():
            raise ValidationError(
                "Program has Projects; archive or reassign before delete."
            )

    def clean(self):
        super().clean()
        if self.pk:
            if not self.name or not self.description:
                raise ValidationError(
                    "Program.Name is required."
                )
    def __str__(self):
        return self.name

