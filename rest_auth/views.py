from http.client import responses
from venv import create
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
def login(request):
    
    try:
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']
    except:
        return Response("No se encontro informacion xp")

    try:
        user = User.objects.get(username=username)
    except:
        return Response("Usuario no encontrado")

    valid_password = check_password(password, user.password)
    if not valid_password:
        return Response("Contraseña incorrecta")
    token, created = Token.objects.get_or_create(user=user)
    print(f"token {token}")
    print(f"token {created}")
    return Response(token.key)