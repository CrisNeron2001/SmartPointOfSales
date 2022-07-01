from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Cliente, Producto, MedioPago, Venta, DetalleVenta

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['id_cliente','nombre','apellidos','correo','direccion']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto','nombre','descripcion','precio']

class MedioPagoForm(ModelForm):
    class Meta:
        model = MedioPago
        fields = ['id_medio_pago','nombre']

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = ['id_venta','monto','medio_pago','fecha','cliente']

class DetalleVentaForm(ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['id_detalle_venta','producto','venta']