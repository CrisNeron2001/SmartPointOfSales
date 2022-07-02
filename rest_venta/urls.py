from django.urls import path
from rest_venta.views import lista_venta, detalle_venta, lista_medio_pago, detalle_medio_pago, lista_detalle_venta, detalle_detalle_venta

urlpatterns = [
    path('lista_venta', lista_venta, name= "lista_venta"),
    path('detalle_venta/<id_venta>', detalle_venta, name="detalle_venta"),
    path('lista_medio_pago', lista_medio_pago, name="lista_medio_pago"),
    path('detalle_medio_pago/<id_medio_pago>', detalle_medio_pago, name="detalle_medio_pago"),
    path('lista_detalle_venta', lista_detalle_venta, name="lista_detalle_venta"),
    path('detalle_detalle_venta/<id_detalle_venta>', detalle_detalle_venta, name="detalle_detalle_venta")
]