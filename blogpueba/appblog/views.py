from django.shortcuts import get_object_or_404, render,  redirect
from django.views.generic import ListView
from django.views.generic.base import View
from .forms import CrearPostForm
from .models import Post

# Create your views here.
class Inicio (ListView):
     
    def get(self, request, *args, **kwargs):

        posts=Post.objects.filter (publicado=True)
        contex={
            'posts': posts
        }
        return render (request, "index.html", contex)


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


class PostView (View):
    def get (self, request, *args, **kwargs):
        context={
            
        }
        return render (request, 'post.html', context)


class CrearPostView(View):
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
                autor=form.cleaned_data.get('autor')
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

