from django.shortcuts import render
from django.http import HttpResponse
from app.forms import formulario as f_formulario
from .models import servicios as f_servicios
from django.shortcuts import render, redirect
from .forms import contactform
from .models import contactform as ModelContactForm  # Importa el modelo correcto


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
    servicios = f_servicios.objects.filter(servicio__icontains=query)  # Ahora 'servicios' hace referencia a la clase
    return render(request, 'app/buscar_form_con_api.html', {'servicios': servicios})

def fcontactform(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            # Guarda los datos del formulario en la base de datos
            ModelContactForm.objects.create(
                Nombre=form.cleaned_data['Nombre'],
                Apellido=form.cleaned_data['Apellido'],
                Email=form.cleaned_data['Email'],
                Telefono=form.cleaned_data['Telefono'],
                Mensaje=form.cleaned_data['Mensaje']
            )
            # Redirige a la página de inicio después de guardar
            return redirect('app/Inicio')  # Asegúrate de que 'app_Inicio' sea la URL correcta para tu página de inicio
    else:
        form = contactform()
    return render(request, 'app/Contacto.html', {'form': form})