from django.urls import path
from .views import listado_view,detalle

urlpatterns = [
    path('',listado_view,name='url_listado'),
    path('<int:numero>',detalle,name='url_detalle')
]