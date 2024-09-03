from django.urls import path, include 
from vbc import views

urlpatterns = [
    path('', views.home),
    path('registrarServicio/', views.registrarServicio, name='registrarServicio'),
    path('edicionServicio/', views.edicionServicio),
    path('editarServicio/', views.editarServicio),
    path('eliminarServicio/', views.eliminarServicio)
]