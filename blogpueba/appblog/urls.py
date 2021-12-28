from django.urls import path
from .views import Inicio, About, BlogListaPost, Contacto,  CrearPostView, Login, Categorias,  Logout, RegistrarUsuario, VerPost

app_name = 'blog' 


urlpatterns = [
    path('', Inicio.as_view(), name= 'index'),
    
    path ('sobrenosotros/', About.as_view(), name='about'),

    path('', BlogListaPost.as_view(), name='lista'),

    path('contacto/', Contacto.as_view(), name='contacto'),

    path ('login/', Login.as_view(), name='login'),

    path ('login/', Logout.as_view(), name='logout'),
    
    path ('crear_post/', CrearPostView.as_view(), name='crear_post'),

    path ('categorias/', Categorias.as_view(), name='categorias'),

    path ('<slug:slug>', VerPost.as_view(), name='ver_post'),

    path ('crear_usuario/', RegistrarUsuario.as_view(), name='registre'),
    
    ]