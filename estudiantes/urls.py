from django.urls import path

from .views import *

urlpatterns = [

    path(
        '',
        lista_estudiantes,
        name='lista_estudiantes'
    ),

    path(
        'crear/',
        crear_estudiante,
        name='crear_estudiante'
    ),

    path(
        'editar/<int:id>/',
        editar_estudiante,
        name='editar_estudiante'
    ),

    path(
        'eliminar/<int:id>/',
        eliminar_estudiante,
        name='eliminar_estudiante'
    ),
]