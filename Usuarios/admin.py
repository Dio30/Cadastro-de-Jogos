from django.contrib import admin
from .models import Perfil

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'imagem_perfil']

admin.site.register(Perfil, PerfilAdmin)
