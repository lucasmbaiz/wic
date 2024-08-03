from django.urls import path
from app import views

urlpatterns = [
    path('Inicio/', views.inicio, name="Inicio"),
    path('Servicios/', views.servicios, name="Servicios"),
    path('Empresa/', views.empresa, name="Empresa"),
    path('Suscripciones/', views.suscripciones, name="Suscripciones"),
    path('Contacto/', views.contacto, name="Contacto"),
    path('Activos/', views.activos, name="Activos"),
    path('Clientes/', views.clientes, name="Clientes"),
    path('Login/', views.login, name="Login"),
    path('formulario/', views.formulario, name='formulario'),
    path('form_con_api/', views.form_con_api, name='FormConApi'),
    path('busqueda_camada/', views.busqueda_camada, name='Busqueda_camada'),
    path('buscar/', views.buscar),
    path('buscar_form_con_api/', views.buscar_form_con_api, name='buscar_form_con_api'), #<<HASTA ACA VENIMOS BIEN>>
    path('mostrar_servicios/', views.mostrar_servicios, name="mostrar_servicios")
]