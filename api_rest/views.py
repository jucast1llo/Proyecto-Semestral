from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import PeliculaProducto, DescripcionProducto, AutorProducto
from .serializers import PeliculaSerializers,PeliculaSerializers2, DescripcionSerializers, DescripcionSerializers2, DirectorSerializers, DirectorSerializers2
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


#### VISTA API PELICULA GET, POST, PUT, DELETE ####

# LISTA PELICULAS #
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_peliculas(request):
    if request.method == 'GET':
        mascotas = PeliculaProducto.objects.all()
        serializer = PeliculaSerializers(mascotas,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PeliculaSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# AGREGAR PELICULAS #
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_pelicula(request):
    data = JSONParser().parse(request)
    serializer = PeliculaSerializers2(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# EIMINAR PELICULAS #
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def Elimpelicula(request,codigo):
    try:
        m = PeliculaProducto.objects.get(codigo = codigo)
    except PeliculaProducto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)   
    if request.method == 'GET':
        serializer = PeliculaSerializers2(m)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PeliculaSerializers2(m,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)     
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
    
#### VISTA API DESCRIPCION GET, POST, PUT, DELETE ####

# LISTA DESCRIPCION #
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_descripcion(request):
    if request.method == 'GET':
        mascotas = DescripcionProducto.objects.all()
        serializer = DescripcionSerializers(mascotas,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PeliculaSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# AGREGAR DESCRIPCION #
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_descripcion(request):
    data = JSONParser().parse(request)
    serializer = DescripcionSerializers2(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# ELIMINAR DESCRIPCION #
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def Elimdescripcion(request,codigo):
    try:
        m = DescripcionProducto.objects.get(codigo = codigo)
    except DescripcionProducto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)  
    if request.method == 'GET':
        serializer = DescripcionSerializers(m)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DescripcionSerializers2(m,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        

#### VISTA API AUTOR GET, POST, PUT, DELETE ####

# LISTA AUTOR #
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_autor(request):
    if request.method == 'GET':
        mascotas = AutorProducto.objects.all()
        serializer = DirectorSerializers(mascotas,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DirectorSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# AGREGAR AUTOR #
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_autor(request):
    data = JSONParser().parse(request)
    serializer = DirectorSerializers2(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# ELIMINAR AUTOR #
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def Elimautor(request,codigo):
    try:
        m = AutorProducto.objects.get(codigo = codigo)
    except AutorProducto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)   
    if request.method == 'GET':
        serializer = DirectorSerializers2(m)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DirectorSerializers2(m,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)      
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)