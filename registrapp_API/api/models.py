from django.db import models

# Create your models here.

class usuario(models.model):
    nombre=models.CharField(max_length=50)
    clase=models.CharField(max_length=50)
    asistencia=models.PositiveBigIntegerField(max_length=50)
