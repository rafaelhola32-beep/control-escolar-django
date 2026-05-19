from django.shortcuts import render, redirect, get_object_or_404

from .models import Calificacion
from .forms import CalificacionForm


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