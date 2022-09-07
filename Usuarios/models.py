from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, default=User, auto_created=True)
    imagem_perfil = models.ImageField(upload_to='perfil', null=True, blank=True, verbose_name='Imagem:')
    
    def __str__(self):
        return self.usuario.username
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        ordering = ['usuario',]
    
    @property
    def image_url(self): # para poder visualizar fotos no html
        if self.imagem_perfil and hasattr(self.imagem_perfil, 'url'):
            return self.imagem_perfil.url