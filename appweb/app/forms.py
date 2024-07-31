from django import forms

class formulario(forms.Form):
    
    #especificar los campos
    servicios = forms.CharField()
    camada = forms.IntegerField()