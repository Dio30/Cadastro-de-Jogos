from django.db import models
from django.contrib.auth.models import User

class Jogos(models.Model):
    nome_do_jogo = models.CharField(max_length=200, verbose_name='Jogo:', unique=False)
    estilo_do_jogo = models.CharField(max_length=50, default='Outros', verbose_name='Estilo:')
    imagem = models.ImageField(null=True, blank=True, verbose_name='Imagem:')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering = ['nome_do_jogo',]
    
    def __str__(self):
        return self.nome_do_jogo
        
    @property
    def image_url(self): # para poder visualizar fotos no html
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url
        
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem_perfil = models.ImageField(upload_to='perfil', null=True, blank=True, verbose_name='Imagem:')
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        ordering = ['usuario',]
    
    @property
    def image_url(self): # para poder visualizar fotos no html
        if self.imagem_perfil and hasattr(self.imagem_perfil, 'url'):
            return self.imagem_perfil.url
        
    def __str__(self):
        return f'{self.usuario.username} Perfil'