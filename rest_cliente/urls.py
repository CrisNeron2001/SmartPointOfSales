from django.urls import path
from rest_cliente.views import lista_cliente, detalle_cliente

urlpatterns = [
    path('lista_cliente', lista_cliente, name='lista_cliente'),
    path('detalle_cliente/<id_cliente>', detalle_cliente, name="detalle_cliente")
]