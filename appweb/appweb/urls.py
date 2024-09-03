from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('vbc/', include('vbc.urls')),
    path('users/', include('users.urls')),
    path('', include('vbc.urls'))
]
# Para archivos estaticos
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)