from django.urls import path

from .views import *

urlpatterns = [

    path(
        '',
        lista_materias,
        name='lista_materias'
    ),

    path(
        'crear/',
        crear_materia,
        name='crear_materia'
    ),

    path(
        'editar/<int:id>/',
        editar_materia,
        name='editar_materia'
    ),

    path(
        'eliminar/<int:id>/',
        eliminar_materia,
        name='eliminar_materia'
    ),
]