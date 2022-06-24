from django.urls import path
from .views import home, contacto, galeria, wallpaper, listausuario, agregar_producto, listar_productos, listacontacto, modificar_producto, eliminar_producto, registro, eliminar_comentario

urlpatterns = [

    ### PELISLANDIA ###

    # MENU PRINCIPAL #
    path('', home,  name="home"),
    path('contacto/', contacto,  name="contacto"),

    # MENU INGRESO USUARIO #
    path('galeria/', galeria,  name="galeria"),
    path('wallpaper/', wallpaper,  name="wallpaper"),

    ### MENU MODIFICACION ADMIN ###
    
    # PELICULAS #
    path('agregar/', agregar_producto,  name="agregar_producto"),
    path('listar/', listar_productos,  name="listar_productos"),
    path('modificar/<id>/', modificar_producto,  name="modificar_producto"),
    path('eliminar/<id>/', eliminar_producto,  name="eliminar_producto"),
    # USUARIOS #
    path('listarcontacto/', listacontacto,  name="listacontacto"),
    path('eliminarcom/<id>/', eliminar_comentario,  name="eliminar_comentario"),
    path('listausuario/', listausuario,  name="listausuario"),
     # REGISTRO #
    path('registro/', registro,  name="registro"),
]
