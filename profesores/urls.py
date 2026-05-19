from django.urls import path

from .views import *

urlpatterns = [

    path(
        '',
        lista_profesores,
        name='lista_profesores'
    ),

    path(
        'crear/',
        crear_profesor,
        name='crear_profesor'
    ),

    path(
        'editar/<int:id>/',
        editar_profesor,
        name='editar_profesor'
    ),

    path(
        'eliminar/<int:id>/',
        eliminar_profesor,
        name='eliminar_profesor'
    ),
]