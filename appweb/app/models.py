from django.db import models

class servicios (models.Model):
    servicio = models.CharField(max_length=40)
    id_servicio = models.IntegerField()

class suscripciones(models.Model):
    suscripcion = models.CharField(max_length=40)
    id_suscripcion = models.IntegerField()

class cliente (models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Email = models.EmailField(max_length=40)
    Telefono = models.CharField(max_length=40)

# Create your models here.
