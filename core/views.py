from django.shortcuts import render, redirect
from http import client
from operator import truediv
from pickle import TRUE
from .models import Cliente, Producto, MedioPago, Venta, DetalleVenta
from .forms import ClienteForm, ProductoForm, MedioPagoForm, VentaForm, DetalleVentaForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def home_cliente(request):
    cliente = Cliente.objects.all()
    data = {
        'cliente': cliente
    }
    return render(request, 'core/home_cliente.html', data)

def home_producto(request):
    producto = Producto.objects.all()
    data = {
        'producto': producto
    }
    return render(request, 'core/home_producto.html', data)

def home_medio_pago(request):
    medioPago = MedioPago.objects.all()
    data = {
        'medioPago': medioPago
    }
    return render(request, 'core/home_medio_pago.html', data)

def home_venta(request):
    venta = Venta.objects.all()
    data = {
        'venta': venta
    }
    return render(request, 'core/home_venta.html', data)

def home_detalle_venta(request):
    detalleVenta = DetalleVenta.objects.all()
    data = {
        'detalleVenta': detalleVenta
    }
    return render(request, 'core/home_detalle_venta.html', data)

#Formularios

def form_cliente(request):
    data = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulary = ClienteForm(request.POST)
        if formulary.is_valid:
            formulary.save()
            data['mensaje'] = "Cliente guardado de forma correcta."
    return render(request, 'core/form_cliente.html', data)

def form_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulary = ProductoForm(request.POST)
        if formulary.is_valid:
            formulary.save()
            data['mensaje'] = "Producto guardado de forma correcta."
    return render(request, 'core/form_producto.html', data)

def form_medio_pago(request):
    data = {
        'form': MedioPagoForm
    }
    if request.method == 'POST':
        formulary = MedioPagoForm(request.POST)
        if formulary.is_valid:
            formulary.save()
            data['mensaje'] = "Medio de pago guardado de forma correcta."
    return render(request, 'core/form_medio_pago.html', data)

def form_venta(request):
    data = {
        'form': VentaForm
    }
    if request.method == 'POST':
        formulary = VentaForm(request.POST)
        if formulary.is_valid:
            formulary.save()
            data['mensaje'] = "Venta guardado de forma correcta."
    return render(request, 'core/form_venta.html', data)

def form_detalle_venta(request):
    data = {
        'form': DetalleVentaForm
    }
    if request.method == 'POST':
        formulary = DetalleVentaForm(request.POST)
        if formulary.is_valid:
            formulary.save()
            data['mensaje'] = "Detalle de venta guardado de forma correcta."
    return render(request, 'core/form_detalle_venta.html', data)

#Formulario de modificacion

def form_mod_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    data = {
        'form': ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulary = ClienteForm(data=request.POST, instance=cliente)
        if formulary.is_valid:
            formulary.save()
            data['mensaje'] = "Cliente se modifico correctamente"
    return render(request, 'core/form_mod_cliente.html', data)

def form_mod_producto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulary = ProductoForm(data=request.POST, instance=producto)
        if formulary.is_valid:
            formulary.save()
            data['mensaje'] = "Producto se modifico correctamente"
        return render(request, 'core/form_mod_producto.html', data)

def form_mod_medio_pago(request, id_medio_pago):
    medioPago = MedioPago.objects.get(id_medio_pago=id_medio_pago)
    data = {
        'form': MedioPagoForm(instance=medioPago)
    }
    if request.method == 'POST':
        formulary = MedioPagoForm(data=request.POST, instance=medioPago)
        if formulary.is_valid:
            formulary.save()
            data['mensaje'] = "Medio de pago se modifico correctamente"
        return render(request, 'core/form_mod_medio_pago.html', data)

def form_mod_venta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    data = {
        'form': VentaForm(instance=venta)
    }
    if request.method == 'POST':
        formulary = VentaForm(data=request.POST, instance=venta)
        if formulary.is_valid:
            formulary.save()
            data['mensaje'] = "Venta se modifico correctamente"
    return render(request, 'core/form_mod_venta.html', data)

#Formulario de eliminacion

def form_del_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect(to='home_cliente')

def form_del_producto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect(to='home_producto')

def form_del_medio_pago(request, id_medio_pago):
    medioPago = MedioPago.objects.get(id_medio_pago=id_medio_pago)
    medioPago.delete()
    return redirect(to='home_medio_pago')

def form_del_venta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect(to='home_venta')