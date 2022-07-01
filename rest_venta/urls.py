from django.urls import path
from rest_venta.views import lista_venta, detalle_venta

urlpatterns = [
    path('lista_venta', lista_venta, name= "lista_venta"),
    path('detalle_venta/<id_venta>', detalle_venta, name="detalle_venta")
]