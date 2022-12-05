from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

escolhas = [
    ('Ação', 'Ação'),
    ('Aventura', 'Aventura'),
    ('Corrida', 'Corrida'),
    ('Futebol', 'Futebol'),
    ('MMORPG', 'MMORPG'),
    ('Outros', 'Outros'),
]

class Jogos(models.Model):
    nome_do_jogo = models.CharField(max_length=200, unique=True, error_messages={"unique": ("Já existe um jogo com este nome!")})
    estoque = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0),
                                       MaxValueValidator(30, message='O valor maximo é de 30 em estoque!')])
    estilo_do_jogo = models.CharField(max_length=50, default='Outros', choices=escolhas, verbose_name='Estilo:')
    imagem = models.ImageField(upload_to='jogos', null=True, blank=True, verbose_name='Imagem:')
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