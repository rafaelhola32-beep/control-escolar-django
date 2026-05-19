from django.urls import path

from .views import *

urlpatterns = [

    path(
        '',
        lista_calificaciones,
        name='lista_calificaciones'
    ),

    path(
        'crear/',
        crear_calificacion,
        name='crear_calificacion'
    ),

    path(
        'editar/<int:id>/',
        editar_calificacion,
        name='editar_calificacion'
    ),

    path(
        'eliminar/<int:id>/',
        eliminar_calificacion,
        name='eliminar_calificacion'
    ),
]