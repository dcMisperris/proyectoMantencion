from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import include


urlpatterns = [
    path('usuario/', views.UsuarioAPIView.as_view()),
    path('usuario/<int:pk>/', views.UsuarioDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
