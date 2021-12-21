from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View

# Create your views here.
class Inicio (ListView):
    
    def get(self, request, *args, **kwargs):
            return render (request, "index.html")


class About (ListView):

    def get (self, request, *args, **kwargs):
        return render (request, 'about.html')

class BlogListaPost (View):
    def get (self, request, *args, **kwargs):
        context={
            
        }
        return render (request, 'lista_posts.html', context)



class Contacto (View):
    def get (self, request, *args, **kwargs):
        context={
            
        }
        return render (request, 'contact.html', context)


class Post (View):
    def get (self, request, *args, **kwargs):
        context={
            
        }
        return render (request, 'post.html', context)