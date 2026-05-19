from django import forms
from .models import Materia

class MateriaForm(forms.ModelForm):

    class Meta:

        model = Materia

        fields = '__all__'

        widgets = {

            'nombre': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'clave': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'creditos': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'carrera': forms.Select(
                attrs={'class': 'form-select'}
            ),
        }