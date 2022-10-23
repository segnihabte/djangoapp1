from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.LandingPage, name="LandingPage"),
    path('names/<str:pk>/' , views.namePro, name="namePro"),
    path('name/', views.naming, name="naming"),
    
]