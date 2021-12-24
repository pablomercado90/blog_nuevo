from django import forms
from django.db.models import fields
from .models import Post
from django.contrib.auth.forms import UserCreationForm
#importa ck editor...leer

class CrearPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('titulo', 'slug', 'descripcion', 'autor', 'categoria', 'contenido', 'imagen_referencial', 'publicado', 'fecha_publicacion')


class CrearUsuario(UserCreationForm):
    pass