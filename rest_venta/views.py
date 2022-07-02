from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Venta, MedioPago, DetalleVenta
from .serializers import VentaSerializer, MedioPagoSerializer, DetalleVentaSerializer
from rest_venta import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt
@permission_classes([IsAuthenticated,])
@api_view(['GET', 'POST'])
def lista_venta(request):
    if request.method == 'GET':
        venta = Venta.objects.all()
        serializer = VentaSerializer(venta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@permission_classes([IsAuthenticated,])
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_venta(request, id_venta):
    try:
        venta = Venta.objects.get(id_venta=id_venta)
    except Venta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VentaSerializer(venta)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(venta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@permission_classes([IsAuthenticated,])
@api_view(['GET', 'POST'])
def lista_medio_pago(request):
    if request.method == 'GET':
        medioPago = MedioPago.objects.all()
        serializer = MedioPagoSerializer(medioPago, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MedioPagoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@permission_classes([IsAuthenticated,])
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_medio_pago(request, id_medio_pago):
    try:
        medioPago = MedioPago.objects.get(id_medio_pago=id_medio_pago)
    except MedioPago.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MedioPagoSerializer(medioPago)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MedioPagoSerializer(medioPago, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        medioPago.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@permission_classes([IsAuthenticated,])
@api_view(['GET', 'POST'])
def lista_detalle_venta(request):
    if request.method == 'GET':
        detalleVenta = DetalleVenta.objects.all()
        serializer = DetalleVentaSerializer(detalleVenta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DetalleVentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@permission_classes([IsAuthenticated,])
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_detalle_venta(request, id_detalle_venta):
    try:
        detalleVenta = DetalleVenta.objects.get(id_detalle_venta=id_detalle_venta)
    except DetalleVenta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DetalleVentaSerializer(detalleVenta)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DetalleVentaSerializer(detalleVenta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        detalleVenta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)