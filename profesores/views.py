from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesor
from .forms import ProfesorForm


def lista_profesores(request):

    profesores = Profesor.objects.all()

    return render(
        request,
        'profesores/lista.html',
        {'profesores': profesores}
    )


def crear_profesor(request):

    formulario = ProfesorForm(request.POST or None)

    if formulario.is_valid():

        formulario.save()

        return redirect('lista_profesores')

    return render(
        request,
        'profesores/crear.html',
        {'formulario': formulario}
    )


def editar_profesor(request, id):

    profesor = get_object_or_404(
        Profesor,
        id=id
    )

    formulario = ProfesorForm(
        request.POST or None,
        instance=profesor
    )

    if formulario.is_valid():

        formulario.save()

        return redirect('lista_profesores')

    return render(
        request,
        'profesores/editar.html',
        {'formulario': formulario}
    )


def eliminar_profesor(request, id):

    profesor = get_object_or_404(
        Profesor,
        id=id
    )

    profesor.delete()

    return redirect('lista_profesores')