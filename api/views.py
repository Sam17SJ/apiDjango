# from django.shortcuts import render
from rest_framework import status, viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.contrib.auth.models import User
from .serializers import *
# Create your views here.

@api_view(['GET','POST'])
def explorer_list(request):
	if request.method=='GET':
		estrella=Estrella.objects.all()
		serializer=EstrellaSerializer(estrella, many=True)
		return Response(serializer.data)
	elif request.method=='POST':
		serializer=EstrellaSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def detalle(request, pk):
	try:
		estrella=Estrella.objects.get(pk=pk)
	except Estrella.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method=='GET':
		serializer=EstrellaSerializer(estrella)
		return Response(serializer.data)
	if request.method=='PUT':
		serializer=EstrellaSerializer(estrella,data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
	elif request.method=='DELETE':
		estrella.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def propiedad_list(request):
	if request.method=='GET':
		propiedad=Propiedad.objects.all()
		serializer=PropiedadSerializer(propiedad, many=True)
		return Response(serializer.data)
	elif request.method=='POST':
		serializer=PropiedadSerializer(data=request.data)
		print(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else: 
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def operacionPropiedad(request, pk):
	try:
		propiedad=Propiedad.objects.get(pk=pk)
	except Propiedad.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method=='GET':
		serializer=PropiedadSerializer(propiedad)
		return Response(serializer.data)
	if request.method=='PUT':
		serializer=PropiedadSerializer(propiedad,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
	elif request.method=='DELETE':
		propiedad.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def user_list(request):
	if request.method=='GET':
		user=User.objects.all()
		serializer=UserSerializer(user, many=True)
		return Response(serializer.data)
	elif request.method=='POST':
		serializer=UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def imageApi(request):
	if request.method=='GET':
		imagenes=Image.objects.all()
		serializer=ImgSerializer(imagenes, many=True)
		return Response(serializer.data)
	elif request.method=='POST':
		serializer =ImgSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			ruta=str(Image.objects.latest('img'))
			print(ruta)

			return Response(ruta, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)