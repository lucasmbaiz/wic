from django.shortcuts import render
from django.http import HttpResponse

from app.forms import formulario as f_formulario

from .models import servicios as f_servicios



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

# Hasta aca genial

def buscar(request):
    
    if request.GET["camada"]:
        
        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada = request.GET['camada']
        servicio = servicio.objects.filter(camada__icontains=camada)
        
        return render(request, "app/resultadobusqueda.hmtl ", {"servicios": servicio, "camada": camada})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

# Hasta acá venimos genial

from app.forms import BuscaServicioForm

def buscar_form_con_api (request):
    if request.method == "POST":
        mi_formulario = BuscaServicioForm(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            servicios = servicios.objects.filter(nombre_icontains=informacion['servicio'])
            
            return render(request, "app/mostrar_servicios.html", {"servicios: servicios"})
    else:
        mi_formulario = BuscaServicioForm()
    
    return render(request, "app/buscar_form_con_api.html", {"mi_formulaio": mi_formulario})

def mostrar_servicios(request):
    return render(request, "app/mostrar_servicios.html")

# Hasta aca venimos bien

from django.shortcuts import render, redirect
from .forms import contactform

def f_contacto(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            contactform.save()
            return redirect('app/Inicio.html')  # Redirige a una página después de guardar
    else:
        form = contactform()
    return render(request, 'app/Contacto.html', {'form': form})

# Este ultimo es para la pagina de contacto