from rest_framework import serializers
from .models import *

class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        #fields = ("id", "nombre", "rut", "idCargo", "idCoordinador")
        fields = '__all__'
