# Generated by Django 2.2.6 on 2020-04-25 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0007_auto_20200403_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='anio',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='enlace_publi',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace publicidad'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='comparte',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='enlacegd',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Google Drive'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='enlacegd2',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Google Drive 2'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='enlacegd3',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Google Drive 3'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='enlacegd4',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Google Drive 4'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='enlacegd5',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Google Drive 5'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='enlacemg',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Mega '),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='enlacemg2',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Mega 2'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='enlacemg3',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Mega 3'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='enlacemg4',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Mega 4'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='enlacemg5',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Mega 5'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='enlacesub',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Subtitulo'),
        ),
    ]
