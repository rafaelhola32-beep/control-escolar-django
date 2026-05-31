from django.shortcuts import render, redirect, get_object_or_404

from .models import Calificacion
from .forms import CalificacionForm

from estudiantes.models import Estudiante
from grupos.models import Grupo


def lista_calificaciones(request):

    calificaciones = Calificacion.objects.all()

    return render(
        request,
        'calificaciones/lista.html',
        {'calificaciones': calificaciones}
    )


def crear_calificacion(request):

    formulario = CalificacionForm(request.POST or None)

    if formulario.is_valid():

        formulario.save()

        return redirect('lista_calificaciones')

    return render(
        request,
        'calificaciones/crear.html',
        {'formulario': formulario}
    )


def editar_calificacion(request, id):

    calificacion = get_object_or_404(
        Calificacion,
        id=id
    )

    formulario = CalificacionForm(
        request.POST or None,
        instance=calificacion
    )

    if formulario.is_valid():

        formulario.save()

        return redirect('lista_calificaciones')

    return render(
        request,
        'calificaciones/editar.html',
        {'formulario': formulario}
    )


def eliminar_calificacion(request, id):

    calificacion = get_object_or_404(
        Calificacion,
        id=id
    )

    calificacion.delete()

    return redirect('lista_calificaciones')


def capturar_calificacion(request, estudiante_id, grupo_id):

    estudiante = get_object_or_404(
        Estudiante,
        id=estudiante_id
    )

    grupo = get_object_or_404(
        Grupo,
        id=grupo_id
    )

    if request.method == 'POST':

        nota = request.POST.get('calificacion')

        Calificacion.objects.create(
            estudiante=estudiante,
            grupo=grupo,
            calificacion=nota
        )

        return redirect(
            'detalle_grupo',
            id=grupo.id
        )

    return render(
        request,
        'calificaciones/capturar.html',
        {
            'estudiante': estudiante,
            'grupo': grupo
        }
    )