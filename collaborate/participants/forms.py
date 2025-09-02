from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = [
            'full_name',
            'email',
            'affiliation',
            'specialization',
            'cross_skill_trained',
            'institution',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'affiliation': forms.Select(attrs={'class': 'form-control'}),
            'specialization': forms.Select(attrs={'class': 'form-control'}),
            'cross_skill_trained': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter institution'}),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'affiliation': 'Affiliation',
            'specialization': 'Specialization',
            'cross_skill_trained': 'Cross-Skill Trained',
            'institution': 'Institution',
        }
