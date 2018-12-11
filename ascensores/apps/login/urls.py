from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    
    path('index/',views.homepage,name = 'home'),
    path('base_layout/',views.base_layout,name ='base_layout')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

