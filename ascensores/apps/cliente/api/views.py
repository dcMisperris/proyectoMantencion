from apps.cliente.models import Cliente
from .serializers import ClienteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404


class ClienteAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cliente/acliente.html'

    def get(self, request):
        cliente = Cliente.objects.all()
        #serializer = ClienteSerializer(cliente, many=True)
        return Response({'cliente':cliente})
        
class ClienteDetailAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cliente/cliente_details.html'

    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        serializer = ClienteSerializer(cliente)
        return Response({'serializer': serializer, 'cliente':cliente})

    def post(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'cliente': cliente})
        serializer.save()
        return redirect('cliente-list')
