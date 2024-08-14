from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('vbc/', include('vbc.urls')),
    path('users/', include('users.urls'))
]
