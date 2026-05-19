from django import forms
from .models import Profesor

class ProfesorForm(forms.ModelForm):

    class Meta:

        model = Profesor

        fields = '__all__'

        widgets = {

            'nombre': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'correo': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),

            'telefono': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }