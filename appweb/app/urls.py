from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Páginas estáticas
    path('Inicio/', views.inicio, name="Inicio"),
    path('Servicios/', views.servicios, name="Servicios"),
    path('Empresa/', views.empresa, name="Empresa"),
    path('Suscripciones/', views.suscripciones, name="Suscripciones"),
    path('Contacto/', views.contacto, name="Contacto"),
    path('Activos/', views.activos, name="Activos"),
    path('Clientes/', views.clientes, name="Clientes"),
    path('Login/', views.login, name="Login"),
    # Formularios
    path('formulario/', views.formulario, name='formulario'),
    path('form_con_api/', views.form_con_api, name='FormConApi'),
    # Busquedas 
    path('busqueda_camada/', views.busqueda_camada, name='Busqueda_camada'),
    path('buscar/', views.buscar_form_con_api, name='buscar_form_con_api'),
    path('buscar_form_con_api/', views.buscar_form_con_api, name='buscar_form_con_api'), #<<HASTA ACA VENIMOS BIEN>>
    path('mostrar_servicios/', views.mostrar_servicios, name='mostrar_servicios')
]
