# Generated by Django 2.2.6 on 2020-05-05 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0012_auto_20200504_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='temporadas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre:')),
                ('nombre_original', models.CharField(max_length=250, verbose_name='Nombre Original:')),
                ('slug_temporada', models.SlugField(blank=True, max_length=250, null=True)),
                ('descripcion', models.CharField(max_length=1000, verbose_name='Descripcion:')),
                ('region', models.CharField(blank=True, max_length=150, null=True)),
                ('Author', models.CharField(max_length=150)),
                ('calificacion', models.CharField(max_length=100)),
                ('descargas', models.IntegerField()),
                ('idiomas', models.CharField(blank=True, choices=[('Español Latino', 'Español Latino'), ('Español Castellano', 'Español Castellano'), ('Español Subtitulado', 'Español Subtitulado'), ('Ingles', 'Ingles')], default=('Español Latino', 'Español Latino'), max_length=150, null=True)),
                ('fecha_estreno', models.DateField(verbose_name='Fecha de Estreno')),
                ('fecha_subida', models.DateField(auto_now_add=True, verbose_name='Fecha de Subida')),
                ('anio', models.CharField(blank=True, max_length=4, null=True)),
                ('trailer', models.CharField(max_length=100)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Subir Imagen 1')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Subir Imagen 2')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Subir Imagen 3')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Subir Imagen 4')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Subir Imagen 5')),
                ('enlacegd', models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace Google Drive')),
                ('comparte', models.CharField(blank=True, max_length=500, null=True)),
                ('enlace_publi', models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace publicidad')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenido.series')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
