from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('index/', inicio, name='index'),
    path('base/', base, name = "base"),
    path('Creador/', CreatePlaca.as_view(), name="Creador"),
    path('Listado/', ListPlaca, name="Listado"),
    path('Modificar/<int:pk>', UpdatePlaca.as_view(), name="Modificar"),
    path('Eliminar/<int:id>',DeletePlacas, name="Eliminar"),
   
]