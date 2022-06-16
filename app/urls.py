from django.db import router
from django.urls import path, include
from .views import home, ProductoViewset, contacto, galeria, wallpaper, listausuario, agregar_producto, listar_productos, listacontacto, modificar_producto, eliminar_producto, registro, eliminar_comentario
from rest_framework import routers

router = routers.DefaultRouter()
router.register('PeliculaProducto', ProductoViewset)

urlpatterns = [
    path('', home,  name="home"),
    path('contacto/', contacto,  name="contacto"),
    path('galeria/', galeria,  name="galeria"),
    path('wallpaper/', wallpaper,  name="wallpaper"),
    path('agregar/', agregar_producto,  name="agregar_producto"),
    path('listar/', listar_productos,  name="listar_productos"),
    path('listarcontacto/', listacontacto,  name="listacontacto"),
    path('modificar/<id>/', modificar_producto,  name="modificar_producto"),
    path('eliminar/<id>/', eliminar_producto,  name="eliminar_producto"),
    path('eliminarcom/<id>/', eliminar_comentario,  name="eliminar_comentario"),
    path('registro/', registro,  name="registro"),
    path('listausuario/', listausuario,  name="listausuario"),
    path('api/', include(router.urls)),
]
