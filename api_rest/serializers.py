from rest_framework import serializers
from app.models import PeliculaProducto

class PeliculaSerializers(serializers.ModelSerializer):
    class Meta:
        model = PeliculaProducto
        fields = ['nombre','codigo','genero','descripcion']


class PeliculaSerializers2(serializers.ModelSerializer):
    class Meta:
        model = PeliculaProducto
        fields = ['nombre','codigo','descripcion','genero']

               