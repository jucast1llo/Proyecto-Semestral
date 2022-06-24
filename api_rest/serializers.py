from rest_framework import serializers
from app.models import PeliculaProducto

# SERIALIZADOR PELICULA # 1
class PeliculaSerializers(serializers.ModelSerializer):
    class Meta:
        model = PeliculaProducto
        fields = ['nombre','codigo','genero','descripcion']

class PeliculaSerializers2(serializers.ModelSerializer):
    class Meta:
        model = PeliculaProducto
        fields = ['nombre','codigo','descripcion','genero']

# SERIALIZADOR DESCRIPION # 2
class DescripcionSerializers(serializers.ModelSerializer):
    class Meta:
        model = PeliculaProducto
        fields = ['genero','codigo','anio','idioma']

class DescripcionSerializers2(serializers.ModelSerializer):
    class Meta:
        model = PeliculaProducto
        fields = ['genero','codigo','anio','idioma']

# SERIALIZADOR DIRECTOR # 3
class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = PeliculaProducto
        fields = ['nombre','codigo','edad']

class DirectorSerializers2(serializers.ModelSerializer):
    class Meta:
        model = PeliculaProducto
        fields = ['nombre','codigo','edad']

               