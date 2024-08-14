from django.db import models

class servicios(models.Model):
    servicio = models.CharField(max_length=40)
    id_servicio = models.IntegerField()
    def __str__(self):
        return self.servicios

class suscripciones(models.Model):
    suscripcion = models.CharField(max_length=40)
    id_suscripcion = models.IntegerField()

class clientes(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Email = models.EmailField(max_length=40)
    Telefono = models.CharField(max_length=40)
    Mensaje = models.TextField(max_length=40, default='')

    def __str__(self):
        return self.Nombre

class activos(models.Model):
    activos = models.CharField(max_length=40)
    id_activos = models.IntegerField()

class formulario(models.Model):
    servicio = models.CharField(max_length=40)
    camada = models.IntegerField()

class Contacto(models.Model): # Este es para el formulario de contacto
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Email = models.EmailField(max_length=40)
    Telefono = models.CharField(max_length=40)
    Mensaje = models.TextField(max_length=400, default='')

    def __str__(self):
        return self.Nombre