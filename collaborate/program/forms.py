from django import forms
from .models import Program

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title', 'description', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }