from django.db import models


# Create your models here.

class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    contrato = models.CharField(max_length=20)
