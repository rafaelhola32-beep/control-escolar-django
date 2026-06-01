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
    
    def clean_profesor (self):

        profesor = self.cleaned_data['profesor']

        if profesor.objects.filter(
            profesor = profesor
        ).exclude(
            pk=self.instance.pk
        ).exists():

            raise forms.ValidationError(
                'Ya existe un Profesor con ese nombre.'
            )

        return profesor
    

