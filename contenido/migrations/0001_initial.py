# Generated by Django 2.2.6 on 2020-04-02 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('slug_categoria', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='peliculas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre:')),
                ('nombre_original', models.CharField(max_length=150, verbose_name='Nombre Original:')),
                ('slug_peliculas', models.SlugField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=1000, verbose_name='Descripcion:')),
                ('region', models.CharField(blank=True, max_length=150, null=True)),
                ('Author', models.CharField(max_length=50)),
                ('calificacion', models.CharField(max_length=100)),
                ('descargas', models.IntegerField()),
                ('idiomas', models.CharField(blank=True, choices=[('Español Latino', 'Español Latino'), ('Español Castellano', 'Español Castellano'), ('Español Subtitulado', 'Español Subtitulado'), ('Ingles', 'Ingles')], default=('Español Latino', 'Español Latino'), max_length=50, null=True)),
                ('fecha_estreno', models.DateField(verbose_name='Fecha de Estreno')),
                ('fecha_subida', models.DateField(verbose_name='Fecha de Subida')),
                ('trailer', models.CharField(max_length=100)),
                ('disco', models.CharField(max_length=250, verbose_name='Peso Archivo')),
                ('reparto', models.CharField(max_length=1000, verbose_name='Reparto')),
                ('online', models.CharField(max_length=500, verbose_name='Link Online')),
                ('img1', models.ImageField(upload_to='', verbose_name='Subir Imagen 1')),
                ('img2', models.ImageField(upload_to='', verbose_name='Subir Imagen 2')),
                ('img3', models.ImageField(upload_to='', verbose_name='Subir Imagen 3')),
                ('img4', models.ImageField(upload_to='', verbose_name='Subir Imagen 4')),
                ('img5', models.ImageField(upload_to='', verbose_name='Subir Imagen 5')),
                ('enlacegd', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive')),
                ('enlacegd2', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 2')),
                ('enlacegd3', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 3')),
                ('enlacegd4', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 4')),
                ('enlacegd5', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 5')),
                ('enlacemg', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega ')),
                ('enlacemg2', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 2')),
                ('enlacemg3', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 3')),
                ('enlacemg4', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 4')),
                ('enlacemg5', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 5')),
                ('comparte', models.CharField(max_length=150)),
                ('genero', models.ManyToManyField(to='contenido.categorias', verbose_name='Genero Juego:')),
            ],
        ),
        migrations.CreateModel(
            name='gamespsx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre:')),
                ('slug_gamespsx', models.SlugField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=1000, verbose_name='Descripcion:')),
                ('region', models.CharField(blank=True, max_length=150, null=True)),
                ('Author', models.CharField(max_length=50)),
                ('calificacion', models.CharField(max_length=100)),
                ('descargas', models.IntegerField()),
                ('idiomas', models.CharField(blank=True, choices=[('Español Latino', 'Español Latino'), ('Español Castellano', 'Español Castellano'), ('Español Subtitulado', 'Español Subtitulado'), ('Ingles', 'Ingles')], default=('Español Latino', 'Español Latino'), max_length=50, null=True)),
                ('fecha_estreno', models.DateField(verbose_name='Fecha de Estreno')),
                ('fecha_subida', models.DateField(verbose_name='Fecha de Subida')),
                ('trailer', models.CharField(max_length=100)),
                ('disco', models.CharField(max_length=250, verbose_name='Peso Archivo')),
                ('img1', models.ImageField(upload_to='', verbose_name='Subir Imagen 1')),
                ('img2', models.ImageField(upload_to='', verbose_name='Subir Imagen 2')),
                ('img3', models.ImageField(upload_to='', verbose_name='Subir Imagen 3')),
                ('img4', models.ImageField(upload_to='', verbose_name='Subir Imagen 4')),
                ('img5', models.ImageField(upload_to='', verbose_name='Subir Imagen 5')),
                ('enlacegd', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive')),
                ('enlacegd2', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 2')),
                ('enlacegd3', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 3')),
                ('enlacegd4', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 4')),
                ('enlacegd5', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 5')),
                ('enlacemg', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega ')),
                ('enlacemg2', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 2')),
                ('enlacemg3', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 3')),
                ('enlacemg4', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 4')),
                ('enlacemg5', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 5')),
                ('comparte', models.CharField(max_length=150)),
                ('genero', models.ManyToManyField(to='contenido.categorias', verbose_name='Genero Juego:')),
            ],
        ),
        migrations.CreateModel(
            name='gamesps3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre:')),
                ('slug_gamesps3', models.SlugField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=1000, verbose_name='Descripcion:')),
                ('region', models.CharField(blank=True, max_length=150, null=True)),
                ('Author', models.CharField(max_length=50)),
                ('calificacion', models.CharField(max_length=100)),
                ('descargas', models.IntegerField()),
                ('idiomas', models.CharField(blank=True, choices=[('Español Latino', 'Español Latino'), ('Español Castellano', 'Español Castellano'), ('Español Subtitulado', 'Español Subtitulado'), ('Ingles', 'Ingles')], default=('Español Latino', 'Español Latino'), max_length=50, null=True)),
                ('fecha_estreno', models.DateField(verbose_name='Fecha de Estreno')),
                ('fecha_subida', models.DateField(verbose_name='Fecha de Subida')),
                ('trailer', models.CharField(max_length=100)),
                ('disco', models.CharField(max_length=250, verbose_name='Peso Archivo')),
                ('cfw', models.CharField(max_length=150, verbose_name='CFW')),
                ('img1', models.ImageField(upload_to='', verbose_name='Subir Imagen 1')),
                ('img2', models.ImageField(upload_to='', verbose_name='Subir Imagen 2')),
                ('img3', models.ImageField(upload_to='', verbose_name='Subir Imagen 3')),
                ('img4', models.ImageField(upload_to='', verbose_name='Subir Imagen 4')),
                ('img5', models.ImageField(upload_to='', verbose_name='Subir Imagen 5')),
                ('enlacegd', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive')),
                ('enlacegd2', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 2')),
                ('enlacegd3', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 3')),
                ('enlacegd4', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 4')),
                ('enlacegd5', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 5')),
                ('enlacemg', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega ')),
                ('enlacemg2', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 2')),
                ('enlacemg3', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 3')),
                ('enlacemg4', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 4')),
                ('enlacemg5', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 5')),
                ('comparte', models.CharField(max_length=150)),
                ('genero', models.ManyToManyField(to='contenido.categorias', verbose_name='Genero Juego:')),
            ],
        ),
        migrations.CreateModel(
            name='gamesps2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre:')),
                ('slug_gamesps2', models.SlugField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=1000, verbose_name='Descripcion:')),
                ('Author', models.CharField(max_length=50)),
                ('calificacion', models.CharField(max_length=100)),
                ('descargas', models.IntegerField()),
                ('idiomas', models.CharField(blank=True, choices=[('Español Latino', 'Español Latino'), ('Español Castellano', 'Español Castellano'), ('Español Subtitulado', 'Español Subtitulado'), ('Ingles', 'Ingles')], default=('Español Latino', 'Español Latino'), max_length=50, null=True)),
                ('fecha_estreno', models.DateField(verbose_name='Fecha de Estreno')),
                ('fecha_subida', models.DateField(verbose_name='Fecha de Subida')),
                ('trailer', models.CharField(max_length=100)),
                ('disco', models.CharField(max_length=250, verbose_name='Peso Archivo')),
                ('region', models.CharField(blank=True, max_length=150, null=True)),
                ('img1', models.ImageField(upload_to='', verbose_name='Subir Imagen 1')),
                ('img2', models.ImageField(upload_to='', verbose_name='Subir Imagen 2')),
                ('img3', models.ImageField(upload_to='', verbose_name='Subir Imagen 3')),
                ('img4', models.ImageField(upload_to='', verbose_name='Subir Imagen 4')),
                ('img5', models.ImageField(upload_to='', verbose_name='Subir Imagen 5')),
                ('enlacegd', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive')),
                ('enlacegd2', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 2')),
                ('enlacegd3', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 3')),
                ('enlacegd4', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 4')),
                ('enlacegd5', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 5')),
                ('enlacemg', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega ')),
                ('enlacemg2', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 2')),
                ('enlacemg3', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 3')),
                ('enlacemg4', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 4')),
                ('enlacemg5', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 5')),
                ('comparte', models.CharField(max_length=150)),
                ('genero', models.ManyToManyField(to='contenido.categorias', verbose_name='Genero Juego:')),
            ],
        ),
        migrations.CreateModel(
            name='gamespc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre:')),
                ('slug_gamespc', models.SlugField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=1000, verbose_name='Descripcion:')),
                ('region', models.CharField(blank=True, max_length=150, null=True)),
                ('Author', models.CharField(max_length=50)),
                ('calificacion', models.CharField(max_length=100)),
                ('descargas', models.IntegerField()),
                ('idiomas', models.CharField(blank=True, choices=[('Español Latino', 'Español Latino'), ('Español Castellano', 'Español Castellano'), ('Español Subtitulado', 'Español Subtitulado'), ('Ingles', 'Ingles')], default=('Español Latino', 'Español Latino'), max_length=50, null=True)),
                ('fecha_estreno', models.DateField(verbose_name='Fecha de Estreno')),
                ('fecha_subida', models.DateField(verbose_name='Fecha de Subida')),
                ('trailer', models.CharField(max_length=100)),
                ('img1', models.ImageField(upload_to='', verbose_name='Subir Imagen 1')),
                ('img2', models.ImageField(upload_to='', verbose_name='Subir Imagen 2')),
                ('img3', models.ImageField(upload_to='', verbose_name='Subir Imagen 3')),
                ('img4', models.ImageField(upload_to='', verbose_name='Subir Imagen 4')),
                ('img5', models.ImageField(upload_to='', verbose_name='Subir Imagen 5')),
                ('procesador', models.CharField(max_length=250, verbose_name='Procesador Requerido')),
                ('so', models.CharField(max_length=250, verbose_name='Sistema Operativo Requerido')),
                ('ram', models.CharField(max_length=250, verbose_name='Memoria RAM Requerida')),
                ('grafica', models.CharField(max_length=250, verbose_name='Tarjeta Grafica Requerida')),
                ('disco', models.CharField(max_length=250, verbose_name='Disco Duro Requerido')),
                ('procesador2', models.CharField(max_length=250, verbose_name='Procesador Recomendado')),
                ('so2', models.CharField(max_length=250, verbose_name='Sistema Operativo Recomendado')),
                ('ram2', models.CharField(max_length=250, verbose_name='Memoria RAM Recomendada')),
                ('grafica2', models.CharField(max_length=250, verbose_name='Tarjeta Grafica Recomendada')),
                ('disco2', models.CharField(max_length=250, verbose_name='Disco Duro Recomendado')),
                ('enlacegd', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive')),
                ('enlacegd2', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 2')),
                ('enlacegd3', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 3')),
                ('enlacegd4', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 4')),
                ('enlacegd5', models.CharField(blank=True, max_length=250, verbose_name='Enlace Google Drive 5')),
                ('enlacemg', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega ')),
                ('enlacemg2', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 2')),
                ('enlacemg3', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 3')),
                ('enlacemg4', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 4')),
                ('enlacemg5', models.CharField(blank=True, max_length=250, verbose_name='Enlace Mega 5')),
                ('comparte', models.CharField(max_length=150)),
                ('genero', models.ManyToManyField(to='contenido.categorias', verbose_name='Genero Juego:')),
            ],
        ),
    ]
