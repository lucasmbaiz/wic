from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from users.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from users.models import Avatar

def login_request(request):
    msg_login = ""
    if request.method == 'POST': 
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "app/Inicio.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/Inicio.html')
        else:
            msg_register = "Error en los datos ingresados. Por favor, revise los campos indicados."
    else:
        form = UserRegisterForm()

    # Solo pasamos el mensaje de registro si hubo un error de validación
    context = {"form": form}
    if 'msg_register' in locals():
        context["msg_register"] = msg_register

    return render(request, "users/registro.html", context)

# Hasta aca vamos bien

@login_required
def editar_usuario(request):
    usuario = request.user
    
    if request.method == "POST":
        formulario = UserEditForm(request.POST, request.FILES, instance=usuario)  # Corrección aquí
        if formulario.is_valid():
            
            if formulario.cleaned_data.get("imagen"):
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data.get("imagen"))
                # usuario.avatar.imagen = formulario.cleaned_data.get("imagen")
                avatar.save()
            
            formulario.save()
            return render(request, "app/Inicio.html")
    else:
        formulario = UserEditForm(instance=usuario)  # Y aquí
    
    return render(request, "users/editar_usuario.html", {"form": formulario })

class CambiarPassView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/cambiar_pass.html"
    success_url = reverse_lazy("EditarUsuario")