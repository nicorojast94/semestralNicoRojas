from django.contrib import admin
from django.urls import path, include
from .views import index,galeria,ubicacion,mision_vision,registro,formulario_insumos,login,cerrar,lista_insumos,eliminar_insumo,buscar,modificar

urlpatterns = [
    path('',index,name='INDEX'),
    path('galeria/',galeria,name='GALERIA'),
    path('ubicacion/',ubicacion,name='UBICACION'),
    path('mision_vision/',mision_vision,name='MISION_VISION'),
    path('registro/',registro,name='REGISTRO'),
    path('formulario_insumos/',formulario_insumos,name='FORMULARIO_INSUMOS'),
    path('login/',login,name='LOGIN'),
    path('logout/',cerrar,name='LOGOUT'),
    path('lista_insumos/',lista_insumos,name='LISTAI'),
    path('eliminar_in/<id>/',eliminar_insumo,name='ELIMINARINSUMO'),
    path('buscar/<id>/',buscar,name='BUSCAR'),
    path('modificar/',modificar,name='MODIFICAR')
]