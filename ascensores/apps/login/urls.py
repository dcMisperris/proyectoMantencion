from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    
    path('index/',views.homepage,name = 'home')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

