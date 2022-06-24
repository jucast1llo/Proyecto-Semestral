from django.contrib import admin
from .models import Pelicula, PeliculaProducto, Contacto

# MODELO VISUALIZAR PELICULA.
class PeliculaProductoEdit(admin.ModelAdmin):
    list_display = ["nombre","codigo","descripcion"]
    list_editable = ["codigo"]
    list_filter = ["codigo"]


# MODELO VISUALIZAR CONTACTO.
class ContactoProductoEdit(admin.ModelAdmin):
    list_display = ["nombre","correo","tipo_consulta","mensaje"]

# MODELOS REGISTRADOS.
admin.site.register(Pelicula)
admin.site.register(PeliculaProducto, PeliculaProductoEdit)
admin.site.register(Contacto, ContactoProductoEdit)

