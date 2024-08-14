from django.urls import path, include
from vbc import views

urlpatterns = [
    path('clientes/listar', views.ClientesListView.as_view(), name="ClientesListar"),
    path('clientes/<pk>', views.ClientesDeleteView.as_view(), name="ClientesBorrar"),
    path('clientes/<pk>/actualizar', views.ClientesUpdateView.as_view(), name="ActualizarClientes"),
]