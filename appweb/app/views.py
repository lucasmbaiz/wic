from django.shortcuts import render
from django.http import HttpResponse
from app.forms import formulario as f_formulario
from .models import servicios as f_servicios
from django.shortcuts import render, redirect
from .forms import contactform
from app.forms import BuscaServicioForm
from .models import servicios


def inicio(request):
    return render(request, "app/Inicio.html")

def empresa(request):
    return render(request, "app/Empresa.html")

def servicios(request):
    return render(request, "app/Servicios.html")

def suscripciones(request):
    return render(request, "app/Suscripciones.html")

def contacto(request):
    return render(request, "app/Contacto.html")

def activos(request):
    return render(request, "app/activos.html")

def clientes(request):
    return render(request, "app/clientes.html")

def login(request):
    return render(request, "app/login.html")

def formulario(request):
    if request.method == 'POST':
        servicios = servicios(nombre=request.POST['servicio'], camada=request.POST['camada'])
        servicios.save()
        
        return render(request, "app/Inicio.html")
    return render(request, "app/formulario.html")

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = f_formulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            servicios = f_servicios(servicio=informacion["servicio"], id_servicio=informacion["camada"])
            servicios.save()

            return render(request, "app/Inicio.html")
            
    else:
        mi_formulario = f_formulario()
        print("## ACÁ SÍ LLEGAMOS ##")
    return render(request, "app/form_con_api.html", {"mi_formulario": mi_formulario})

def busqueda_camada(request):
    return render(request, "app/busqueda_camada.html")

def buscar(request):
    respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
    
    return HttpResponse(respuesta)

# Hasta acá venimos genial

def mostrar_servicios(request):
    return render(request, "app/mostrar_servicios.html")

# Hasta aca venimos bien

def buscar_form_con_api(request):
    query = request.GET.get('q', '')
    servicios = servicios.objects.filter(servicio__icontains=query)  # Ahora 'servicios' hace referencia a la clase
    return render(request, 'buscar_form_con_api.html', {'servicios': servicios})


def f_contacto(request):
    if request.method == 'GET':
        form = contactform(request.GET)
        if form.is_valid():
            contactform.save()
            return redirect('app/Inicio.html')  # Redirige a una página después de guardar
    else:
        form = contactform()
    return render(request, 'app/Contacto.html', {'form': form})

# Este ultimo es para la pagina de contacto