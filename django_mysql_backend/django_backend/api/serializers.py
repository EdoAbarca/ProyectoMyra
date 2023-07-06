from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		return user

class UserLoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('email', 'password')
	##
	def check_credentials(self, clean_data):
		user = authenticate(email=clean_data['email'], password=clean_data['password'])
		if not user:
			raise ValidationError('Autenticación rechazada')
		return user

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username', 'is_superuser', 'is_staff', 'is_active','date_joined', 'last_login')
		#fields = '__all__'


class CargoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cargo
		fields = '__all__'

class ProfesionalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profesional
		fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    #sername_field = 'email'
	pass
