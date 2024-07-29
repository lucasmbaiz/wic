from django import forms

class formulario(forms.Form):
    
    #especificar los campos
    servicio = forms.CharField()
    camada = forms.IntegerField()