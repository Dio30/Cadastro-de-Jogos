# Generated by Django 4.0.5 on 2022-12-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jogos', '0004_jogos_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogos',
            name='slug',
            field=models.SlugField(blank=True, default=1, unique=True),
            preserve_default=False,
        ),
    ]
