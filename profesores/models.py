from django.db import models

class Profesor(models.Model):

    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    correo = models.EmailField()

    telefono = models.CharField(
        max_length=15
    )

    def __str__(self):
        return self.nombre