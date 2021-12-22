from django import forms
from django.db.models import fields
from .models import Post

class CrearPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('titulo', 'slug', 'descripcion', 'autor', 'categoria', 'contenido', 'imagen_referencial', 'publicado', 'fecha_publicacion')