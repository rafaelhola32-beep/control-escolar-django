from django.db import models

class Aula(models.Model):

    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre