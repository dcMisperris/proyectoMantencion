from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def agregarCliente(request):
    return render(request,'cliente/acliente.html')
