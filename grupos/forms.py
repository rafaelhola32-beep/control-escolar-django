from django import forms
from .models import Grupo

class GrupoForm(forms.ModelForm):

    class Meta:

        model = Grupo

        fields = '__all__'

        widgets = {

            'nombre': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'profesor': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'materia': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'aula': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'horario': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'periodo': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'estudiantes': forms.SelectMultiple(
                attrs={
                    'class': 'form-select'
                }
            ),
        }