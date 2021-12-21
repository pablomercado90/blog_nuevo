from django.urls import path
from .views import Inicio, About, BlogListaPost, Contacto, Post

app_name = 'blog' 


urlpatterns = [
    path('', Inicio.as_view(), name= 'index'),
    
    path ('sobrenosotros/', About.as_view(), name='about'),

    path('', BlogListaPost.as_view(), name='lista'),

    path('contacto/', Contacto.as_view(), name='contacto'),

    path ('post/', Post.as_view(), name='post'),
    
    ]