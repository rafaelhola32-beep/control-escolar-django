from django.shortcuts import render, redirect, get_object_or_404

from .models import Grupo
from .forms import GrupoForm


def lista_grupos(request):

    grupos = Grupo.objects.all()

    return render(
        request,
        'grupos/lista.html',
        {'grupos': grupos}
    )


def crear_grupo(request):

    formulario = GrupoForm(request.POST or None)

    if formulario.is_valid():

        formulario.save()

        return redirect('lista_grupos')

    return render(
        request,
        'grupos/crear.html',
        {'formulario': formulario}
    )


def editar_grupo(request, id):

    grupo = get_object_or_404(
        Grupo,
        id=id
    )

    formulario = GrupoForm(
        request.POST or None,
        instance=grupo
    )

    if formulario.is_valid():

        formulario.save()

        return redirect('lista_grupos')

    return render(
        request,
        'grupos/editar.html',
        {'formulario': formulario}
    )


def eliminar_grupo(request, id):

    grupo = get_object_or_404(
        Grupo,
        id=id
    )

    grupo.delete()

    return redirect('lista_grupos')


def detalle_grupo(request, id):

    grupo = get_object_or_404(
        Grupo,
        id=id
    )

    estudiantes = grupo.estudiantes.all()

    return render(
        request,
        'grupos/detalle.html',
        {
            'grupo': grupo,
            'estudiantes': estudiantes
        }
    )