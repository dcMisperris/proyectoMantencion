from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    # path('cliente/',views.agregarCliente,name='agregar-cliente'),
    path('cliente/registro/',views.RegistroCliente,name='registro-cliente'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)