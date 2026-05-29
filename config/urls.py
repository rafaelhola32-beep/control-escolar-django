from django.contrib import admin
from django.urls import path, include

from config import views

urlpatterns = [

    # INICIO
    path(
        '',
        views.inicio,
        name='inicio'
    ),

    # ADMIN
    path(
        'admin/',
        admin.site.urls
    ),

    # ESTUDIANTES
    path(
        'estudiantes/',
        include('estudiantes.urls')
    ),

    # PROFESORES
    path(
        'profesores/',
        include('profesores.urls')
    ),

    # MATERIAS
    path(
        'materias/',
        include('materias.urls')
    ),

    # GRUPOS
    path(
        'grupos/',
        include('grupos.urls')
    ),

    # CALIFICACIONES
    path(
        'calificaciones/',
        include('calificaciones.urls')
    ),

]