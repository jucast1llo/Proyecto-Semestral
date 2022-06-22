from django.urls import path
from api_rest.views import lista_peliculas,agregar_pelicula,Elimpelicula
from api_rest.viewsLogin import login

urlpatterns = [
    path('lista_peliculas/',lista_peliculas,name="lista_peliculas"),
    path('agregar_pelicula/',agregar_pelicula,name="agregar_pelicula"),
    path('Elimpelicula/<codigo>',Elimpelicula,name="Elimpelicula"),
]