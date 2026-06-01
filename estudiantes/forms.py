from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):

    class Meta:

        model = Estudiante

        fields = '__all__'

        widgets = {

            'nombre': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'matricula': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'correo': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),

            'carrera': forms.Select(
                attrs={'class': 'form-select'}
            ),
        }

    def clean_matricula(self):

        matricula = self.cleaned_data['matricula']

        if Estudiante.objects.filter(
            matricula=matricula
        ).exclude(
            pk=self.instance.pk
        ).exists():

            raise forms.ValidationError(
                'Ya existe un estudiante con esa matrícula.'
            )

        return matricula