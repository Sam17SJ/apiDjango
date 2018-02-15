from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class EstrellaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estrella
        fields = '__all__'

class PropiedadSerializer(serializers.ModelSerializer):
	# img= serializers.ImageField(max_length=None, use_url=True)
	class Meta:
		model = Propiedad
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model= User
		fields= '__all__'

class ImgSerializer(serializers.ModelSerializer):
	img= serializers.ImageField(max_length=None, use_url=True)
	class Meta:
		model= Image
		fields= '__all__'