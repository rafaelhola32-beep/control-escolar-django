from django.shortcuts import render, redirect, get_object_or_404

from .models import Grupo
from estudiantes.models import Estudiante
from calificaciones.models import Calificacion


def detalle_grupo(request, id):

    grupo = get_object_or_404(
        Grupo,
        id=id
    )

    calificaciones = Calificacion.objects.filter(
        grupo=grupo
    )

    context = {

        'grupo': grupo,
        'calificaciones': calificaciones

    }

    return render(
        request,
        'grupos/detalle.html',
        context
    )