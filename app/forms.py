from django import forms
from .models import Contacto, PeliculaProducto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# FORMULARIO DE CONTACTO #
class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=15) #VALIDACION 1
    class Meta:
        model = Contacto
        fields = '__all__'

# FORMULARIO DE AGREGAR PELICULAS #
class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=30) #VALIDACION 1
    descripcion = forms.CharField(required=False) #VALIDACION 2

    class Meta:
        model = PeliculaProducto
        fields = '__all__'
        Widgets = {
                "fecha_pelicula": forms.SelectDateWidget()
        }

# FORMULARIO DE REGISTRO #
class CustomUserCreation(UserCreationForm):
    email = forms.CharField(required=True) #VALIDACION 1
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
