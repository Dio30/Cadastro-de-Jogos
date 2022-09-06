from django.contrib import admin
from .models import Jogos, Perfil

class JogosAdmin(admin.ModelAdmin):
    list_display = ['nome_do_jogo', 'estilo_do_jogo', 'imagem', 'usuario']

admin.site.register(Jogos, JogosAdmin)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['imagem_perfil', 'usuario']

admin.site.register(Perfil, PerfilAdmin)