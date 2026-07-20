"""
URL configuration for TRAZABILIDAD_ESTERILIZACION project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('examinar/',include('examinar.urls')),
    path('',home,name='url_home'),
    path('about',about,name='url_about')
]

"""
Lo siguiente habilita acceder a los archivos guardados en la carpeta 'media'
cuando se use la url MEDIA_URL, es decir /media/
por ejemplo http://127.0.0.1:8000/media/1.pdf
"""
from django.conf.urls.static import static
from django.conf import settings  ## esto es el objeto configuración que incluye las propiedades incluidas en settings.py

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)