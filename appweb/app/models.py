from django.db import models

class servicios(models.Model):
    servicio = models.CharField(max_length=40)
    id_servicio = models.IntegerField()
    def __str__(self):
        return self.nombre

class suscripciones(models.Model):
    suscripcion = models.CharField(max_length=40)
    id_suscripcion = models.IntegerField()

class clientes(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Email = models.EmailField(max_length=40)
    Telefono = models.CharField(max_length=40)

class activos(models.Model):
    activos = models.CharField(max_length=40)
    id_activos = models.IntegerField()

class formulario(models.Model):
    servicio = models.CharField(max_length=40)
    camada = models.IntegerField()