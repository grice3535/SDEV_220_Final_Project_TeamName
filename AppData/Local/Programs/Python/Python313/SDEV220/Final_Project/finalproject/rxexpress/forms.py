from django import forms
from .models import Patient, Prescription

class PatientCheck(forms.ModelForm):
    class Meta:
        model = Patient, Prescription
        fields = ['first_name', 'last_name', 'date_of_birth', 'medication_name']
        widgets = {

            'first_name': forms.TextInput(attrs={'class': 'form-control'}),

            'last_name': forms.TextInput(attrs={'class': 'form-control'}),

            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'medication_name': forms.TextInput(attrs={'class': 'form-control'}),



        } 