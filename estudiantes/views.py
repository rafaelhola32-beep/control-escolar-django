from django.shortcuts import render, redirect, get_object_or_404

from .models import Estudiante
from .forms import EstudianteForm


def lista_estudiantes(request):

    estudiantes = Estudiante.objects.all()

    return render(
        request,
        'estudiantes/lista.html',
        {'estudiantes': estudiantes}
    )


def crear_estudiante(request):

    formulario = EstudianteForm(request.POST or None)

    if formulario.is_valid():

        formulario.save()

        return redirect('lista_estudiantes')

    return render(
        request,
        'estudiantes/crear.html',
        {'formulario': formulario}
    )


def editar_estudiante(request, id):

    estudiante = get_object_or_404(
        Estudiante,
        id=id
    )

    formulario = EstudianteForm(
        request.POST or None,
        instance=estudiante
    )

    if formulario.is_valid():

        formulario.save()

        return redirect('lista_estudiantes')

    return render(
        request,
        'estudiantes/editar.html',
        {
            'formulario': formulario
        }
    )


def eliminar_estudiante(request, id):

    estudiante = get_object_or_404(
        Estudiante,
        id=id
    )

    estudiante.delete()

    return redirect('lista_estudiantes')