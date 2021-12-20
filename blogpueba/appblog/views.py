from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class Inicio (ListView):
    
    def get(self, request, *args, **kwargs):
            return render (request, "index.html")

def about (request):
    return render (request, 'about.html')