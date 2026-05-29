from django.shortcuts import render

from estudiantes.models import Estudiante
from profesores.models import Profesor
from materias.models import Materia
from grupos.models import Grupo



def inicio(request):

    total_estudiantes = Estudiante.objects.count()

    total_profesores = Profesor.objects.count()

    total_materias = Materia.objects.count()

    total_grupos = Grupo.objects.count()

    contexto = {

        'total_estudiantes': total_estudiantes,
        'total_profesores': total_profesores,
        'total_materias': total_materias,
        'total_grupos': total_grupos,
    }

    return render(
        request,
        'inicio.html',
        contexto
    )