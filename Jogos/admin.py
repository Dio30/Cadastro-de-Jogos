from django.contrib import admin
from .models import Jogos

class JogosAdmin(admin.ModelAdmin):
    list_display = ['nome_do_jogo', 'estoque', 'estilo_do_jogo', 'imagem', 'usuario']
    readonly_fields = ['usuario']

admin.site.register(Jogos, JogosAdmin)