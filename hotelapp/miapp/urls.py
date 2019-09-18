from django.urls import path
from .views import *

urlpatterns = [
    path("",index, name = "index"), 
    path("habitacion/", habitacionList.as_view(), name = "Listarhabitacion"),
    path('habitacion/nuevo/', habitacionCreate.as_view(), name = 'nuevohabitacion'),
    path('habitacion/editar/<int:pk>', habitacionUpdate.as_view(), name = 'editarhabitacion'),
    path('habitacion/eliminar/<int:pk>', habitacionDelete.as_view(), name = 'eliminarhabitacion'),
    path('habitacion/detalle/<int:pk>', habitacionDetalle.as_view(), name = 'detallehabitacion'),
    path('pago/nuevo/', pagoCreate.as_view(), name = 'nuevo_pago'),
    path('pagos/', pagoList.as_view(), name = 'lista_pago'),]
