from django.urls import path, include 
from vbc import views

urlpatterns = [
    path('', views.home),
    path('registrarServicio/', views.registrarServicio, name='registrarServicio'),
    path('edicionServicio/<id>', views.edicionServicio, name='edicionServicio'),
    path('editarServicio/', views.editarServicio, name='editarServicio'),
    path('eliminarServicio/<id>', views.eliminarServicio, name='eliminarServicio')
]