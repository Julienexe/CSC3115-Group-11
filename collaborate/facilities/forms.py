from django import forms
from .models import Facility, Service, Equipment

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'location', 'description', 'partner_organization', 'facility_type', 'capabilities']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'partner_organization': forms.TextInput(attrs={'class': 'form-control'}),
            'facility_type': forms.Select(attrs={'class': 'form-control'}),
            'capabilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['facility', 'name', 'description', 'category', 'skill_type']
        widgets = {
            'facility': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'skill_type': forms.Select(attrs={'class': 'form-control'}),
        }

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['facility', 'name', 'capabilities', 'description', 'inventory_code', 'usage_domain', 'support_phase']
        widgets = {
            'facility': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'capabilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'inventory_code': forms.TextInput(attrs={'class': 'form-control'}),
            'usage_domain': forms.Select(attrs={'class': 'form-control'}),
            'support_phase': forms.Select(attrs={'class': 'form-control'}),
        }