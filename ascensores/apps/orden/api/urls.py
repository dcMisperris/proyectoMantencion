from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    path('orden-api/',views.ordenListView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)