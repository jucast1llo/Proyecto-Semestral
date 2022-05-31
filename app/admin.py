from django.contrib import admin
from .models import Pelicula, PeliculaProducto, Contacto

class PeliculaProductoEdit(admin.ModelAdmin):
    list_display = ["nombre","codigo","descripcion"]
    list_editable = ["codigo"]
    list_filter = ["codigo"]

class ContactoProductoEdit(admin.ModelAdmin):
    list_display = ["nombrecontacto","correo","tipo_consulta","mensaje"]

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(PeliculaProducto, PeliculaProductoEdit)
admin.site.register(Contacto, ContactoProductoEdit)

