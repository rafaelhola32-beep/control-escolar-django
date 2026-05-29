from django.urls import path

from .views import *

urlpatterns = [

    path(
        '',
        lista_grupos,
        name='lista_grupos'
    ),

    path(
        'crear/',
        crear_grupo,
        name='crear_grupo'
    ),

    path(
        'editar/<int:id>/',
        editar_grupo,
        name='editar_grupo'
    ),

    path(
        'eliminar/<int:id>/',
        eliminar_grupo,
        name='eliminar_grupo'
    ),

    path(
        'detalle/<int:id>/',
        detalle_grupo,
        name='detalle_grupo'
    ),

]