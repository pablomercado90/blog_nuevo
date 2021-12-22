from django.urls import path
from .views import Inicio, About, BlogListaPost, Contacto,  CrearPostView, PostView

app_name = 'blog' 


urlpatterns = [
    path('', Inicio.as_view(), name= 'index'),
    
    path ('sobrenosotros/', About.as_view(), name='about'),

    path('', BlogListaPost.as_view(), name='lista'),

    path('contacto/', Contacto.as_view(), name='contacto'),

    path ('post/', PostView.as_view(), name='post'),
    
    path ('crear_post/', CrearPostView.as_view(), name='crear_post')
    
    ]