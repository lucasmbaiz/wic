from django.contrib import admin
from .models import activos, clientes, servicios

# Register your models here.
admin.site.register(activos)
admin.site.register(clientes)
admin.site.register(servicios)