# Generated by Django 4.1 on 2022-08-31 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jogos', '0002_alter_jogos_estilo_do_jogo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jogos',
            options={'ordering': ['nome_do_jogo'], 'verbose_name': 'Jogo', 'verbose_name_plural': 'Jogos'},
        ),
        migrations.AlterField(
            model_name='jogos',
            name='estilo_do_jogo',
            field=models.CharField(default='Outros', max_length=50, verbose_name='Estilo:'),
        ),
        migrations.AlterField(
            model_name='jogos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagem:'),
        ),
        migrations.AlterField(
            model_name='jogos',
            name='nome_do_jogo',
            field=models.CharField(max_length=200, unique=True, verbose_name='Jogo:'),
        ),
    ]
