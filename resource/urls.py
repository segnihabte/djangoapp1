from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.LandingPage, name="LandingPage"),
    path('names/' , views.names, name="names"),
    path('list/<str:pk>/', views.list, name="list"),
]