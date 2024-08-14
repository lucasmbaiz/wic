from django.contrib import admin
from .models import activos, clientes, servicios, Contacto

# Register your models here.
admin.site.register(activos)
admin.site.register(clientes)
admin.site.register(servicios)
admin.site.register(Contacto)