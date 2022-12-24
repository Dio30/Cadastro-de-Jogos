from django.contrib import admin
from .models import Jogos

class JogosAdmin(admin.ModelAdmin):
    list_display = ['nome_do_jogo', 'estilo_do_jogo', 'estoque', 'imagem', 'usuario']
    readonly_fields = ['usuario', 'slug']

admin.site.register(Jogos, JogosAdmin)