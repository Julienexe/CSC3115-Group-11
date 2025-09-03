from django import forms
from .models import Project, Outcome

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'program',
            'facility',
            'title',
            'nature_of_project',
            'description',
            'innovation_focus',
            'prototype_stage',
            'testing_requirements',
            'commercialization_plan'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'testing_requirements': forms.Textarea(attrs={'rows': 3}),
            'commercialization_plan': forms.Textarea(attrs={'rows': 3}),
        }

class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = [
            'project',
            'title',
            'description',
            'artifact_link',
            'outcome_type',
            'quality_certification',
            'commercialization_status'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'artifact_link': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }