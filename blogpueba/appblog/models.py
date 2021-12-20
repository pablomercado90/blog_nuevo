from datetime import time
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET
from django.db.models.fields import TextField
from django.db.models.manager import Manager
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class ModeloBase(models.Model):
    id=models.AutoField(primary_key=True)
    estado=models.BooleanField('Estado', default=True)
    fecha_creacion=models.DateTimeField ('Fecha creación', auto_now=False, auto_now_add= True)
    fecha_modificacion=models.DateTimeField ('Fecha de modificación', auto_now= True, auto_now_add= False)
    fecha_eliminacion=models.DateTimeField ('Fecha de eliminación', auto_now=True, auto_now_add= False)

    class Meta:
        abstract = True


class Categoria(ModeloBase):
    nombre=models.CharField('Nombre de la categoría', max_length=100, unique = True)
    imagen_ref=models.ImageField ('Imagen referencial', upload_to = 'categoria/')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(ModeloBase):
    nombre=models.CharField('Nombres', max_length=250)
    apellido=models.CharField('Apellido', max_length=250)
    email=models.CharField('Correo electrónico', max_length=250)
    descripcion=models.TextField('Descripción')
    web=models.URLField ('Web', null=True, blank=True)
    facebook=models.URLField ('Facebook', null=True, blank=True)
    twitter=models.URLField ('Twitter', null=True, blank=True)
    instagram=models.URLField ('Instagram', null=True, blank=True)

    def __str__(self):
        return self.nombre

        
class Post(ModeloBase):
    titulo=models.CharField ('Título del post', max_length=200, unique=True)
    slug=models.CharField ('Slug', max_length=150, unique=True)
    descripcion=models.TextField ('Descripción')
    autor=models.ForeignKey (Autor, on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido=RichTextField()
    imagen_referencial=models.ImageField ('Imagen referencial', upload_to='imagenes/', max_length=255)
    publicado=models.BooleanField ('Publicado / no publicado', default=False)
    fecha_publicacion=models.DateField ('Fecha de publicación')
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo 
        
  
class Comentario(ModeloBase):
    autor=models.CharField(max_length=100)
    comentario=models.CharField(max_length=500)
    email=models.CharField(max_length=100)
    creacion=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.autor


class Web (ModeloBase):
    nosotros=models.TextField('Nosotros')
    tel=models.CharField('Teléfono', max_length=15)
    email=models.EmailField('Correo Electrónico', max_length=200)
    direccion=models.CharField('Dirección', max_length=200)

    class Meta:
        verbose_name='Web'
        verbose_name_plural='Webs'

class RedesSociales(ModeloBase):
    facebook=models.URLField ('Facebook')
    twitter=models.URLField ('Twitter')
    instagram=models.URLField ('Instagram')

    class Meta:
        verbose_name='Red Social'
        verbose_name_plural='Redes Sociales'

    def __str__(self):
        return self.facebook


class Contacto(ModeloBase):
    nombre=models.CharField ('Nombre', max_length=150)
    apellido=models.CharField('Apellido', max_length=100)
    correo=models.EmailField('Correo Electrónico', max_length=150)
    asunto=models.CharField('Asunto', max_length=150)
    mensaje=models.TextField ('Mensaje')

    class Meta:
        verbose_name='Contacto'
        verbose_name_plural='Contactos'

    def __str__(self):
        return self.asunto

class Suscriptores (ModeloBase):
    correo=models.EmailField('Correo Electrónico', max_length=200)

    class Meta:
        verbose_name='Suscriptor'
        verbose_name_plural='Suscriptores'

    def __str__(self):
        return self.correo