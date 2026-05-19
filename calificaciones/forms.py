from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):

    class Meta:

        model = Calificacion

        fields = '__all__'

        widgets = {

            'estudiante': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'grupo': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'calificacion': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
        }