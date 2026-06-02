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

    def clean_nombre(self):

        nombre = self.cleaned_data['nombre']

        if Materia.objects.filter(
            nombre=nombre
        ).exclude(
            pk=self.instance.pk
        ).exists():

            raise forms.ValidationError(
                'Ya existe una materia con ese nombre.'
            )

        return nombre