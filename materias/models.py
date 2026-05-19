from django.db import models
from carreras.models import Carrera

class Materia(models.Model):

    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=20)
    creditos = models.IntegerField()

    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre