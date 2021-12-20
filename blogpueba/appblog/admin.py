from django.contrib import admin
from .models import *


class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'estado', 'fecha_creacion')
    search_field=['nombre']
    
class AutorAdmin(admin.ModelAdmin):
    list_display=('nombre', 'apellido', 'email', 'estado', 'fecha_creacion')
    search_field=['nombre', 'apellido', 'email']



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Web)
admin.site.register(RedesSociales)
admin.site.register(Contacto)
admin.site.register(Suscriptores)




