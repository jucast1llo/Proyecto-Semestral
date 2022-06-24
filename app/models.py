from audioop import maxpp
from distutils.command.upload import upload
from mailbox import NoSuchMailboxError
from pyexpat import model
from django.db import models
from django.forms import CharField

# MODELO GENERO PELICULA #
class Pelicula(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# MODELO PELICULA #
class PeliculaProducto (models.Model):
    nombre = models.CharField(max_length=15)
    codigo = models.IntegerField()
    descripcion = models.TextField()
    genero = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="peliculas", null=True)
    urlpelicula = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

# MODELO DESCRIPCION #
class DescripcionProducto (models.Model):
    idioma = models.CharField(max_length=15)
    codigo = models.IntegerField()
    anio = models.IntegerField()
    genero = models.ForeignKey(Pelicula, on_delete=models.PROTECT)


    def __str__(self):
        return self.nombre

# MODELO AUTOR #
class AutorProducto (models.Model):
    nombre = models.CharField(max_length=15)
    codigo = models.IntegerField()
    edad = models.IntegerField()


    def __str__(self):
        return self.nombre

# CONSULTAS CONTACTO #
opciones_consultas = [
    [0, "Consultas"],
    [1, "Sugerencias"],
    [2, "Recuperacion"],
    [3, "Agradecimientos"]
]        

# MODELO CONTACTO #
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre