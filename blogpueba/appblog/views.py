from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import get_object_or_404, render,  redirect
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from .forms import CrearPostForm, CrearUsuario
from django.contrib.auth.models import User
from .models import Categoria, Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

# Create your views here.
class Inicio (ListView):
    def get(self, request, *args, **kwargs):
        filtro=request.GET.get('buscar', '')
        posts=Post.objects.filter (publicado=True).filter (titulo__icontains=filtro)

        contex={
            'posts': posts
        }
        return render (request, "index.html", contex)


class VerPost(DetailView):
    def get (self, request, slug, *args, **kwargs):
        try:
            verposts=Post.objects.get (slug=slug)
        except:
            verposts=None
        context={
            'verposts': verposts,
        }
        return render (request, 'post.html', context)



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


class Login (View):
    def get (self, request, *args, **kwargs):
        
        context={
           
        }
        return render (request, 'registration/login.html', context)


class Logout (View):
    def get (self, request, *args, **kwargs):
        
        context={
           
        }
        return render (request, 'registration/login.html', context)




class CrearPostView(LoginRequiredMixin, View):
    def get (self, request, *args, **kwargs):
        form=CrearPostForm()
        context={
            'form':form          
        }
        return render (request, 'crearpost.html', context)

    def post (self, request, *args, **kwargs):
        if request.method == "POST":
            form = CrearPostForm (request.POST)
            if form.is_valid ():
                titulo = form.cleaned_data.get('titulo')
                slug=form.cleaned_data.get('slug')
                descripcion=form.cleaned_data.get('descripcion')
                autor=request.user
                categoria=form.cleaned_data.get('categoria')
                contenido=form.cleaned_data.get('contenido')
                imagen_referencial=form.cleaned_data.get('imagen_referencial')
                publicado=form.cleaned_data.get('publicado')
                fecha_publicacion=form.cleaned_data.get ('fecha_publicacion')
                p, created=Post.objects.get_or_create (titulo=titulo, slug=slug, descripcion=descripcion, autor=autor, categoria=categoria, contenido=contenido, imagen_referencial=imagen_referencial, publicado=publicado, fecha_publicacion=fecha_publicacion)
                p.save()
                return redirect('blog:index') 

        context={ 

        }
        return render (request, 'crearpost.html', context)

class Categorias (ListView):
     model=Categoria
     template_name = 'categorias.html'

    # def get(self, request, *args, **kwargs):
    #     contex={

    #     }
        
    #     return render (request, "categorias.html", contex)


class RegistrarUsuario(CreateView):
    # model=User
    # template_name='registration/registre.html'
    # form_class=CrearUsuario
    # success_url= reverse_lazy ('blog:index')




    def get (self, request, *args, **kwargs):
        form=CrearUsuario()
        context={
            'form':form          
        }
        return render (request, 'registration/registre.html', context)

    def post (self, request, *args, **kwargs):
        if request.method == "POST":
            form = CrearUsuario (request.POST)
            if form.is_valid ():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password1']
                form.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect ('blog:index')

        context={ 

        }
        return render (request, 'index.html', context)    

