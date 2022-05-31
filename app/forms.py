from django import forms
from .models import Contacto, PeliculaProducto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# FORMULARIO DE CONTACTO #
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

# FORMULARIO DE AGREGAR PELICULAS #
class ProductoForm(forms.ModelForm):
    class Meta:
        model = PeliculaProducto
        fields = '__all__'
        Widgets = {
                "fecha_pelicula": forms.SelectDateWidget()
        }

# FORMULARIO DE REGISTRO #
class CustomUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
