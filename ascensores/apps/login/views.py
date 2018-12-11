from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario
from apps.login.api.serializers import UsuarioSerializer
from django.http import JsonResponse
import json

# Create your views here.

def homepage (request):
    return render(request,'login/login.html')