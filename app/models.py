from audioop import maxpp
from distutils.command.upload import upload
from mailbox import NoSuchMailboxError
from pyexpat import model
from django.db import models
from django.forms import CharField

########## MODELOS/CLASES PELISLANDIA ##########

# CLASE PELICULA #
class Pelicula(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# CLASE PELICULA/ATRIBUTOS #
class PeliculaProducto (models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
    descripcion = models.TextField()
    genero = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="peliculas", null=True)
    urlpelicula = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

# OPCIONES DE CONTACTO #
opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Recuperacion"],
    [4, "Agradecimientos"],
]        


# CLASE CONTACTO/ATRIBUTOS #
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre
