from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
idioma=(
    ("Español Latino","Español Latino"),
    ("Español Castellano","Español Castellano"),
    ("Español Subtitulado","Español Subtitulado"),
    ("Ingles","Ingles"),
)
class categorias(models.Model):
    nombre=models.CharField(max_length=100)
    slug_categoria=models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.slug_categoria
def slug_generator_categoria(sender,instance,*args,**kwargs):
    if instance.slug_categoria:
        return
    instance.slug_categoria=slugify(instance.nombre)
pre_save.connect(slug_generator_categoria,sender=categorias)
class  gamespc(models.Model):
    nombre=models.CharField(max_length=150,verbose_name="Nombre:")
    slug_gamespc=models.SlugField(null=True,blank=True)
    descripcion=models.CharField(max_length=1000,verbose_name="Descripcion:")
    genero=models.ManyToManyField(categorias,verbose_name="Genero Juego:")
    region=models.CharField(max_length=150,blank=True,null=True)
    Author=models.CharField(max_length=50)
    calificacion=models.CharField(max_length=100)
    descargas=models.IntegerField()
    idiomas=models.CharField(max_length=50,choices=idioma,null=True,blank=True,default=idioma[0])
    fecha_estreno=models.DateField(verbose_name="Fecha de Estreno")
    fecha_subida=models.DateField(verbose_name="Fecha de Subida")
    trailer=models.CharField(max_length=100)
    img1=models.ImageField(verbose_name="Subir Imagen 1",blank=True,null=True)
    img2=models.ImageField(verbose_name="Subir Imagen 2",blank=True,null=True)
    img3=models.ImageField(verbose_name="Subir Imagen 3",blank=True,null=True)
    img4=models.ImageField(verbose_name="Subir Imagen 4",blank=True,null=True)
    img5=models.ImageField(verbose_name="Subir Imagen 5",blank=True,null=True)
    procesador=models.CharField(max_length=250,verbose_name="Procesador Requerido")
    so=models.CharField(max_length=250,verbose_name="Sistema Operativo Requerido")
    ram=models.CharField(max_length=250,verbose_name="Memoria RAM Requerida")
    grafica=models.CharField(max_length=250,verbose_name="Tarjeta Grafica Requerida")
    disco=models.CharField(max_length=250,verbose_name="Disco Duro Requerido")
    procesador2=models.CharField(max_length=250,verbose_name="Procesador Recomendado")
    so2=models.CharField(max_length=250,verbose_name="Sistema Operativo Recomendado")
    ram2=models.CharField(max_length=250,verbose_name="Memoria RAM Recomendada")
    grafica2=models.CharField(max_length=250,verbose_name="Tarjeta Grafica Recomendada")
    disco2=models.CharField(max_length=250,verbose_name="Disco Duro Recomendado")
    enlacegd=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive")
    enlacegd2=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 2")
    enlacegd3=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 3")
    enlacegd4=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 4")
    enlacegd5=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 5")
    enlacemg=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega ")
    enlacemg2=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 2")
    enlacemg3=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 3")
    enlacemg4=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 4")
    enlacemg5=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 5")
    comparte=models.CharField(max_length=150)
    def __str__(self):
            return self.nombre
def slug_generator_gamespc(sender,instance,*args,**kwargs):
    if instance.slug_gamespc:
        return
    instance.slug_gamespc=slugify(instance.nombre)
pre_save.connect(slug_generator_gamespc,sender=gamespc)

class  gamespsx(models.Model):
    nombre=models.CharField(max_length=150,verbose_name="Nombre:")
    slug_gamespsx=models.SlugField(null=True,blank=True)
    descripcion=models.CharField(max_length=1000,verbose_name="Descripcion:")
    genero=models.ManyToManyField(categorias,verbose_name="Genero Juego:")
    region=models.CharField(max_length=150,blank=True,null=True)
    Author=models.CharField(max_length=50)
    calificacion=models.CharField(max_length=100)
    descargas=models.IntegerField()
    idiomas=models.CharField(max_length=50,choices=idioma,null=True,blank=True,default=idioma[0])
    fecha_estreno=models.DateField(verbose_name="Fecha de Estreno")
    fecha_subida=models.DateField(verbose_name="Fecha de Subida")
    trailer=models.CharField(max_length=100)
    disco=models.CharField(max_length=250,verbose_name="Peso Archivo")
    img1=models.ImageField(verbose_name="Subir Imagen 1",blank=True,null=True)
    img2=models.ImageField(verbose_name="Subir Imagen 2",blank=True,null=True)
    img3=models.ImageField(verbose_name="Subir Imagen 3",blank=True,null=True)
    img4=models.ImageField(verbose_name="Subir Imagen 4",blank=True,null=True)
    img5=models.ImageField(verbose_name="Subir Imagen 5",blank=True,null=True)
    enlacegd=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive")
    enlacegd2=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 2")
    enlacegd3=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 3")
    enlacegd4=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 4")
    enlacegd5=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 5")
    enlacemg=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega ")
    enlacemg2=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 2")
    enlacemg3=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 3")
    enlacemg4=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 4")
    enlacemg5=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 5")
    comparte=models.CharField(max_length=150)
    def __str__(self):
            return self.nombre
def slug_generator_gamespsx(sender,instance,*args,**kwargs):
    if instance.slug_gamespsx:
        return
    instance.slug_gamespsx=slugify(instance.nombre)
pre_save.connect(slug_generator_gamespsx,sender=gamespsx)
class  gamesps2(models.Model):
    nombre=models.CharField(max_length=150,verbose_name="Nombre:")
    slug_gamesps2=models.SlugField(null=True,blank=True)
    descripcion=models.CharField(max_length=1000,verbose_name="Descripcion:")
    genero=models.ManyToManyField(categorias,verbose_name="Genero Juego:")
    Author=models.CharField(max_length=50)
    calificacion=models.CharField(max_length=100)
    descargas=models.IntegerField()
    idiomas=models.CharField(max_length=50,choices=idioma,null=True,blank=True,default=idioma[0])
    fecha_estreno=models.DateField(verbose_name="Fecha de Estreno")
    fecha_subida=models.DateField(verbose_name="Fecha de Subida")
    trailer=models.CharField(max_length=100)
    disco=models.CharField(max_length=250,verbose_name="Peso Archivo")
    region=models.CharField(max_length=150,blank=True,null=True)
    img1=models.ImageField(verbose_name="Subir Imagen 1",blank=True,null=True)
    img2=models.ImageField(verbose_name="Subir Imagen 2",blank=True,null=True)
    img3=models.ImageField(verbose_name="Subir Imagen 3",blank=True,null=True)
    img4=models.ImageField(verbose_name="Subir Imagen 4",blank=True,null=True)
    img5=models.ImageField(verbose_name="Subir Imagen 5",blank=True,null=True)
    enlacegd=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive")
    enlacegd2=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 2")
    enlacegd3=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 3")
    enlacegd4=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 4")
    enlacegd5=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 5")
    enlacemg=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega ")
    enlacemg2=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 2")
    enlacemg3=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 3")
    enlacemg4=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 4")
    enlacemg5=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 5")
    comparte=models.CharField(max_length=150)
    def __str__(self):
            return self.nombre
def slug_generator_gamesps2(sender,instance,*args,**kwargs):
    if instance.slug_gamesps2:
        return
    instance.slug_gamesps2=slugify(instance.nombre)
pre_save.connect(slug_generator_gamesps2,sender=gamesps2)

class  gamesps3(models.Model):
    nombre=models.CharField(max_length=150,verbose_name="Nombre:")
    slug_gamesps3=models.SlugField(null=True,blank=True)
    descripcion=models.CharField(max_length=1000,verbose_name="Descripcion:")
    genero=models.ManyToManyField(categorias,verbose_name="Genero Juego:")
    region=models.CharField(max_length=150,blank=True,null=True)
    Author=models.CharField(max_length=50)
    calificacion=models.CharField(max_length=100)
    descargas=models.IntegerField()
    idiomas=models.CharField(max_length=50,choices=idioma,null=True,blank=True,default=idioma[0])
    fecha_estreno=models.DateField(verbose_name="Fecha de Estreno")
    fecha_subida=models.DateField(verbose_name="Fecha de Subida")
    trailer=models.CharField(max_length=100)
    disco=models.CharField(max_length=250,verbose_name="Peso Archivo")
    cfw=models.CharField(max_length=150,verbose_name="CFW")
    img1=models.ImageField(verbose_name="Subir Imagen 1",blank=True,null=True)
    img2=models.ImageField(verbose_name="Subir Imagen 2",blank=True,null=True)
    img3=models.ImageField(verbose_name="Subir Imagen 3",blank=True,null=True)
    img4=models.ImageField(verbose_name="Subir Imagen 4",blank=True,null=True)
    img5=models.ImageField(verbose_name="Subir Imagen 5",blank=True,null=True)
    enlacegd=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive")
    enlacegd2=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 2")
    enlacegd3=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 3")
    enlacegd4=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 4")
    enlacegd5=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 5")
    enlacemg=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega ")
    enlacemg2=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 2")
    enlacemg3=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 3")
    enlacemg4=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 4")
    enlacemg5=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 5")
    comparte=models.CharField(max_length=150)
    def __str__(self):
            return self.nombre
def slug_generator_gamesps3(sender,instance,*args,**kwargs):
    if instance.slug_gamesps3:
        return
    instance.slug_gamesps3=slugify(instance.nombre)
pre_save.connect(slug_generator_gamesps3,sender=gamesps3)

class  peliculas(models.Model):
    nombre=models.CharField(max_length=250,verbose_name="Nombre:")
    nombre_original=models.CharField(max_length=250,verbose_name="Nombre Original:")
    slug_peliculas=models.SlugField(max_length=250,null=True,blank=True)
    descripcion=models.CharField(max_length=1000,verbose_name="Descripcion:")
    genero=models.ManyToManyField(categorias,verbose_name="Genero Juego:")
    region=models.CharField(max_length=150,blank=True,null=True)
    Author=models.CharField(max_length=150)
    calificacion=models.CharField(max_length=100)
    descargas=models.IntegerField()
    idiomas=models.CharField(max_length=150,choices=idioma,null=True,blank=True,default=idioma[0])
    fecha_estreno=models.DateField(verbose_name="Fecha de Estreno")
    fecha_subida=models.DateField(verbose_name="Fecha de Subida")
    trailer=models.CharField(max_length=100)
    disco=models.CharField(max_length=250,verbose_name="Peso Archivo")
    director=models.CharField(max_length=100,verbose_name="Director")
    reparto=models.CharField(max_length=1000,verbose_name="Reparto")
    online=models.CharField(max_length=500,verbose_name="Link Online")
    img1=models.ImageField(verbose_name="Subir Imagen 1",blank=True,null=True)
    img2=models.ImageField(verbose_name="Subir Imagen 2",blank=True,null=True)
    img3=models.ImageField(verbose_name="Subir Imagen 3",blank=True,null=True)
    img4=models.ImageField(verbose_name="Subir Imagen 4",blank=True,null=True)
    img5=models.ImageField(verbose_name="Subir Imagen 5",blank=True,null=True)
    enlacegd=models.CharField(max_length=250,blank=True,null=True,verbose_name="Enlace Google Drive")
    enlacegd2=models.CharField(max_length=250,blank=True,null=True,verbose_name="Enlace Google Drive 2")
    enlacegd3=models.CharField(max_length=250,blank=True,null=True,verbose_name="Enlace Google Drive 3")
    enlacegd4=models.CharField(max_length=250,blank=True,null=True,verbose_name="Enlace Google Drive 4")
    enlacegd5=models.CharField(max_length=250,blank=True,null=True,verbose_name="Enlace Google Drive 5")
    enlacesub=models.CharField(max_length=250,blank=True,null=True,verbose_name="Enlace Subtitulo")
    enlacemg=models.CharField(max_length=250,blank=True,null=True,verbose_name="Enlace Mega ")
    enlacemg2=models.CharField(max_length=250,blank=True,null=True,verbose_name="Enlace Mega 2")
    enlacemg3=models.CharField(max_length=250,blank=True,null=True,verbose_name="Enlace Mega 3")
    enlacemg4=models.CharField(max_length=250,blank=True,null=True,verbose_name="Enlace Mega 4")
    enlacemg5=models.CharField(max_length=250,blank=True,null=True,verbose_name="Enlace Mega 5")
    comparte=models.CharField(max_length=250,blank=True,null=True)
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('pelicula', kwargs={'slug': self.slug_peliculas})
def slug_generator_peliculas(sender,instance,*args,**kwargs):
    if instance.slug_peliculas:
        return
    instance.slug_peliculas=slugify(instance.nombre)
pre_save.connect(slug_generator_peliculas,sender=peliculas)
