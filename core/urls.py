from django.contrib import admin
from django.urls import path, include

# para mostrar imagens no modo debug 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lista.urls')),
]

# NAO USAR EM PRODUCAO
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
