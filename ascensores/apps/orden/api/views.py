from rest_framework.generics import ListCreateAPIView
from .serializers import OrdenSerializer
from apps.orden.models import Orden
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class ordenListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    
    # def get(self, request, format=None):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    #return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = OrdenSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    