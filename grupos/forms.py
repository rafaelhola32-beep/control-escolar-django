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

            'carrera': forms.Select(
                attrs={'class': 'form-select'}
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

    def clean_nombre(self):

        nombre = self.cleaned_data['nombre']

        if Grupo.objects.filter(
            nombre=nombre
        ).exclude(
            pk=self.instance.pk
        ).exists():

            raise forms.ValidationError(
                'Ya existe un grupo con ese nombre.'
            )

        return nombre