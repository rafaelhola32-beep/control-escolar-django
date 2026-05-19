from django.db import models
from carreras.models import Carrera

class Estudiante(models.Model):

    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    correo = models.EmailField()

    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre