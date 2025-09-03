from django import forms
from .models import Program

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'description', 'national_alignment', 'focus_areas', 'phases']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'national_alignment': forms.TextInput(attrs={'class': 'form-control'}),
            'focus_areas': forms.TextInput(attrs={'class': 'form-control'}),
            'phases': forms.TextInput(attrs={'class': 'form-control'}),
        }