from django.urls import path
from .views import Inicio, about



urlpatterns = [
    path('', Inicio.as_view(), name= 'index'),

]