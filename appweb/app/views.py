from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Vista Inicio")

def servicios(request):
    return HttpResponse("Vista Servicios")

def suscripciones(request):
    return HttpResponse("Vista Suscripciones")

def contacto(request):
    return HttpResponse("Vista Contacto")

# Create your views here.
    