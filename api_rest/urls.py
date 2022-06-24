from django.urls import path
from api_rest.views import lista_peliculas,agregar_pelicula,Elimpelicula, lista_descripcion,agregar_descripcion, Elimdescripcion, lista_autor, agregar_autor, Elimautor
from api_rest.viewsLogin import login

urlpatterns = [
    # API  PELICULAS #
    path('lista_peliculas/',lista_peliculas,name="lista_peliculas"),
    path('agregar_pelicula/',agregar_pelicula,name="agregar_pelicula"),
    path('Elimpelicula/<codigo>',Elimpelicula,name="Elimpelicula"),
    # API  DESCRIPCION #
    path('lista_descripcion/',lista_descripcion,name="lista_descripcion"),
    path('agregar_descripcion/',agregar_descripcion,name="agregar_descripcion"),
    path('Elimdescripcion/<codigo>',Elimdescripcion,name="Elimdescripcion"),
    # API  AUTOR #
    path('lista_autor/',lista_autor,name="lista_autor"),
    path('agregar_autor/',agregar_autor,name="agregar_autor"),
    path('Elimautor/<codigo>',Elimautor,name="Elimautor"),
]