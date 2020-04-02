# Generated by Django 3.0 on 2020-04-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0004_auto_20200402_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='comparte',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='nombre',
            field=models.CharField(max_length=250, verbose_name='Nombre:'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='nombre_original',
            field=models.CharField(max_length=250, verbose_name='Nombre Original:'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='slug_peliculas',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
