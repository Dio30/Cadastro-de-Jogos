# Generated by Django 4.0.5 on 2022-12-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jogos', '0003_alter_jogos_estoque_alter_jogos_nome_do_jogo'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogos',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]