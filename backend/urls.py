from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    url(r'^list/',views.List, name='list'),
    url(r'^model/',views.Model, name='model')
]