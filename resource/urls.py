from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('names/' , views.names, name="names"),
    path('list/<str:pk>/', views.list, name="list"),
]