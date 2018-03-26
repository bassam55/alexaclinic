from django import forms
from EyeChart.models import Patient

class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
