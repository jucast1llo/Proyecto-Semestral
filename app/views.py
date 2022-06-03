from dataclasses import dataclass
import re
from urllib import request
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import PeliculaProducto, Contacto
from .forms import ContactoForm, ProductoForm, CustomUserCreation
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages



# INICIO #
def home(request):
    productos = PeliculaProducto.objects.all()
    data = { 
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def Contactopeli(request):
    productos = Contacto.objects.all()
    data = { 
        'productos': productos
    }
    return render(request, 'app/listacontacto.html', data)

# CONTACTO #
def contacto(request):
    data = {
        'form':ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje Enviado!")
        else:
            data["form"] = formulario
    return render(request, 'app/contacto.html', data)

# GALERIA #
def galeria(request):
    productos = PeliculaProducto.objects.all()
    data = { 
        'productos': productos
    }
    return render(request, 'app/galeria.html', data)

# GALERIA#
def wallpaper(request):
    productos = PeliculaProducto.objects.all()
    data = { 
        'productos': productos
    }
    return render(request, 'app/wallpaper.html', data)

# AGREGAR #
@permission_required('app.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Pelicula Agregada")
        else:
            data["form"] = formulario
    return render(request, 'app/producto/agregar.html', data)

# LISTAR PELICULAS #
@permission_required('app.view_producto')
def listar_productos(request):
    productos = PeliculaProducto.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(productos, 3)
        productos = paginator.page(page)
    except:
        raise Http404

    data = { 
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'app/producto/listar.html', data)

# LISTAR PELICULAS #
@permission_required('app.view_producto')
def listacontacto(request):
    productos = Contacto.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(productos, 3)
        productos = paginator.page(page)
    except:
        raise Http404

    data = { 
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'app/producto/listacontacto.html', data)

# MODIFICAR #
@permission_required('app.change_producto')
def modificar_producto(request, id):
    producto = get_object_or_404(PeliculaProducto, id=id)
    data = { 
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificacion Exitosa")
            return redirect(to="listar_productos")
        data["form"] = formulario   
    return render(request, 'app/producto/modificar.html', data)

# ELIMINAR PELICULA #
@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(PeliculaProducto, id=id)
    producto.delete()
    return redirect(to="listar_productos")

# ELIMINAR COMENTARIO #
@permission_required('app.delete_producto')
def eliminar_comentario(request, id):
    producto = get_object_or_404(Contacto, id=id)
    producto.delete()
    return redirect(to="listacontacto")

# REGISTRO #
def registro(request):
    data = { 
        'form': CustomUserCreation()
    }

    if request.method == 'POST':
        formulario = CustomUserCreation(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registracion Exitosa, Bienvenido")
            return redirect(to="home")
        data["form"] = formulario 
    return render(request, 'registration/registro.html', data)