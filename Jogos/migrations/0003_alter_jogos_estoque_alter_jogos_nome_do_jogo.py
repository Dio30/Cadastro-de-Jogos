# Generated by Django 4.0.5 on 2022-12-10 18:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jogos', '0002_jogos_estoque_alter_jogos_nome_do_jogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogos',
            name='estoque',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30, message='O valor maximo é de 30 em estoque!')], verbose_name='Quant. em Estoque'),
        ),
        migrations.AlterField(
            model_name='jogos',
            name='nome_do_jogo',
            field=models.CharField(error_messages={'unique': 'Já existe um jogo com este nome!'}, max_length=200, unique=True),
        ),
    ]
