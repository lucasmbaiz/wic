from django import forms
from django.db import models
from .models import Contacto

class formulario(forms.Form):
    
    #especificar los campos
    servicio = forms.CharField()
    camada = forms.IntegerField()

# Hasta aca venimos bien

class BuscaServicioForm(forms.Form):
    servicio = forms.CharField(max_length=40)
    camada = forms.IntegerField

# Hasta aca venimos bien

class contactform(forms.ModelForm):
    class Meta:
        model = Contacto
        # fields = ['Nombre', 'Apellido', 'Email', 'Telefono', 'Mensaje']
        fields = '__all__'