from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import include


urlpatterns = [
    path('apicliente/', views.ClienteAPIView.as_view()),
    path('apicliente/<int:pk>/', views.ClienteDetailAPIView.as_view()),
    path('clienteapi-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)