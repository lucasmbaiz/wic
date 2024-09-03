from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.models import clientes
from .models import ServicioList
from django.contrib import messages

def home(request):
    servicioapp = ServicioList.objects.all()
    return render(request, "servicios_crear.html", {"ServicioList": servicioapp} )

def registrarServicio(request):
    id=request.POST['txtid']
    nombre=request.POST['txtnombre']
    valoracion=request.POST['numvaloracion']
    
    servicio = ServicioList.objects.create(
        id=id, nombre=nombre, valoracion=valoracion)
    return redirect('/')

def edicionServicio(request, codigo):
    servicio = ServicioList.objects.get(id=id)
    return render(request, "edicionServicio.html", {"servicio": servicio})


def editarServicio(request):
    id = request.POST['txtid']
    nombre = request.POST['txtnombre']
    valoracion = request.POST['numvaloracion']

    servicio = ServicioList.objects.get(id=id)
    ServicioList.nombre = nombre
    ServicioList.valoracion = valoracion
    ServicioList.save()

    messages.success(request, '¡Servicio actualizado!')

    return redirect('/')

def eliminarServicio(request, id):
    servicio = ServicioList.objects.get(id=id)
    ServicioList.delete()

    messages.success(request, '¡Servicio eliminado!')

    return redirect('/')