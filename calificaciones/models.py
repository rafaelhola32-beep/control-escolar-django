from django.db import models

from estudiantes.models import Estudiante
from grupos.models import Grupo


class Calificacion(models.Model):

    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE
    )

    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.CASCADE
    )

    calificacion = models.DecimalField(
        max_digits=4,
        decimal_places=1
    )

    def __str__(self):
        return str(self.calificacion)