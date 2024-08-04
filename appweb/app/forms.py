from django import forms
from django.db import models
from .models import contactform

class formulario(forms.Form):
    
    #especificar los campos
    servicio = forms.CharField()
    camada = forms.IntegerField()

# Hasta aca venimos bien

class BuscaServicioForm(forms.Form):
    servicio = forms.CharField(max_length=40)
    camada = forms.IntegerField

# Hasta aca venimos bien

# class clientes(forms.Form):
    # Nombre = models.CharField(max_length=40)
    # Apellido = models.CharField(max_length=40)
    # Email = models.EmailField(max_length=40)
    # Telefono = models.CharField(max_length=40)
    # Mensaje = models.TextField(max_length=40)

    # def __str__(self):
        # return self.name
# Este ultimo es para el html del contacto

class contactform(forms.Form):
    class Meta:
        model = contactform
        fields = ['Nombre', 'Apellido' 'Email', 'Telefono', 'Mensaje']