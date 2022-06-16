from dataclasses import field, fields
from .models import PeliculaProducto
from rest_framework import serializers

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PeliculaProducto
        fields = '__all__'