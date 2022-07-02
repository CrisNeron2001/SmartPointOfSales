from dataclasses import field, fields
from rest_framework import serializers
from core.models import Venta,MedioPago,DetalleVenta

class VentaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Venta
        fields = ['id_venta', 'monto', 'medio_pago', 'fecha', 'cliente']
class MedioPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedioPago
        fields = ['id_medio_pago', 'nombre']
class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ['id_detalle_venta', 'producto', 'venta']