from users import views
from django.contrib.auth.views import LogoutView
from django.urls import path


urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name="app/Inicio.html"), name="Logout"), # Hasta aca vamos bien
    path('editar_usuario/', views.editar_usuario, name="EditarUsuario"),
    path('cambiar_pass/', views.CambiarPassView.as_view(), name="CambiarPass")
]