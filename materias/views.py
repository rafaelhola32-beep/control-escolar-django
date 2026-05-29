from django.shortcuts import render, redirect, get_object_or_404
from .models import Materia
from .forms import MateriaForm


def lista_materias(request):

    materias = Materia.objects.all()

    return render(
        request,
        'materias/lista.html',
        {'materias': materias}
    )


def crear_materia(request):

    formulario = MateriaForm(request.POST or None)

    if formulario.is_valid():

        formulario.save()

        return redirect('lista_materias')

    return render(
        request,
        'materias/crear.html',
        {'formulario': formulario}
    )


def editar_materia(request, id):

    materia = get_object_or_404(
        Materia,
        id=id
    )

    formulario = MateriaForm(
        request.POST or None,
        instance=materia
    )

    if formulario.is_valid():

        formulario.save()

        return redirect('lista_materias')

    return render(
        request,
        'materias/editar.html',
        {'formulario': formulario}
    )


def eliminar_materia(request, id):

    materia = get_object_or_404(
        Materia,
        id=id
    )

    materia.delete()

    return redirect('lista_materias')