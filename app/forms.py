from lib2to3.refactor import MultiprocessRefactoringTool
from django import forms
from .models import Contacto, PeliculaProducto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


########## FORMULARIOS PELISLANDIA ##########

# FORMULARIO DE CONTACTO #
class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=5, max_length=50)  # VALIDACION 1
    class Meta:
        model = Contacto
        fields = '__all__'

# FORMULARIO DE PELICULAS #
class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=5, max_length=50)  # VALIDACION 1
    imagen = forms.ImageField(required=False)              # VALIDACION 2
    urlpelicula = forms.CharField(required=False)          # VALIDACION 3
    class Meta:
        model = PeliculaProducto
        fields = '__all__'
        Widgets = {
                "fecha_pelicula": forms.SelectDateWidget()
        }

# FORMULARIO DE REGISTRO #
class CustomUserCreation(UserCreationForm):
    usuario = forms.CharField(min_length=5, max_length=15) # VALIDACION 1
    class Meta:
        model = User
        fields = ['usuario','first_name','last_name','email','password1','password2']
