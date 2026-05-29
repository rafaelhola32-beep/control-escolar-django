from django.db import models

from profesores.models import Profesor
from materias.models import Materia
from aulas.models import Aula
from horarios.models import Horario
from periodos.models import Periodo
from estudiantes.models import Estudiante
from carreras.models import Carrera


class Grupo(models.Model):

    nombre = models.CharField(max_length=50)

    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.CASCADE
    )

    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE
    )

    aula = models.ForeignKey(
        Aula,
        on_delete=models.CASCADE
    )

    horario = models.ForeignKey(
        Horario,
        on_delete=models.CASCADE
    )

    periodo = models.ForeignKey(
        Periodo,
        on_delete=models.CASCADE
    )

    estudiantes = models.ManyToManyField(
        Estudiante
    )
        # NUEVO CAMPO
    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre