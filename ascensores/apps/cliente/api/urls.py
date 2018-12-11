from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import include


urlpatterns = [
    path('apicliente/', views.ClienteAPIView.as_view(),name='cliente-list'),
    path('apicliente/<int:pk>/', views.ClienteDetailAPIView.as_view(),name='cliente-details'),
    path('clienteapi-auth/', include('rest_framework.urls')),
    #path('registrocli/',views.RegistroCliente.as_view(),name='regisro-cliente'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
