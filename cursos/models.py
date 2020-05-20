from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
import datetime
# Create your models here.
idioma=(
    ("Español Latino","Español Latino"),
    ("Español Castellano","Español Castellano"),
    ("Español Subtitulado","Español Subtitulado"),
    ("Ingles","Ingles"),
)
class categorias_cursos(models.Model):
    nombre=models.CharField(max_length=100)
    slug_categoria_cur=models.SlugField(null=True,blank=True)
    class Meta:
        ordering = ['nombre',]
    def __str__(self):
        return self.nombre
def slug_generator_categorias_cursos(sender,instance,*args,**kwargs):
    if instance.slug_categoria_cur:
        return
    instance.slug_categoria_cur=slugify(instance.nombre)
pre_save.connect(slug_generator_categorias_cursos,sender=categorias_cursos)

class lenguaje_cursos(models.Model):
    nombre=models.CharField(max_length=100)
    slug_categoria_len=models.SlugField(null=True,blank=True)
    class Meta:
        ordering = ['nombre',]
    def __str__(self):
        return self.nombre
def slug_generator_lenguaje_cursos(sender,instance,*args,**kwargs):
    if instance.slug_categoria_len:
        return
    instance.slug_categoria_len=slugify(instance.nombre)
pre_save.connect(slug_generator_lenguaje_cursos,sender=lenguaje_cursos)

class plataforma_cursos(models.Model):
    nombre=models.CharField(max_length=100)
    slug_categoria_pla=models.SlugField(null=True,blank=True)
    class Meta:
        ordering = ['nombre',]
    def __str__(self):
        return self.nombre
def slug_generator_plataforma_cursos(sender,instance,*args,**kwargs):
    if instance.slug_categoria_pla:
        return
    instance.slug_categoria_pla=slugify(instance.nombre)
pre_save.connect(slug_generator_plataforma_cursos,sender=plataforma_cursos)

class cursos(models.Model):
    nombre=models.CharField(max_length=250,verbose_name="Nombre:")
    nombre_original=models.CharField(max_length=250,verbose_name="Nombre Original:")
    slug_curso=models.SlugField(max_length=250,null=True,blank=True)
    descripcion=models.CharField(max_length=1000,verbose_name="Descripcion:")
    descripcion_resumida=models.CharField(max_length=150,verbose_name="Descripcion:", null=True,blank=True)
    plataforma=models.ForeignKey(plataforma_cursos,on_delete=models.CASCADE,verbose_name="Indicar la Plataforma de Cursos:")
    genero=models.ManyToManyField(categorias_cursos,verbose_name="Generios Cursos:")
    lenguaje=models.ManyToManyField(lenguaje_cursos,verbose_name="Lenguaje Cursos:",null=True,blank=True)
    Author=models.CharField(max_length=150)
    calificacion=models.CharField(max_length=100)
    descargas=models.IntegerField()
    idiomas=models.CharField(max_length=150,choices=idioma,null=True,blank=True,default=idioma[0])
    fecha_estreno=models.DateField(verbose_name="Fecha del Curso")
    fecha_subida=models.DateField(verbose_name="Fecha de Subida",auto_now_add=True)
    anio=models.CharField(max_length=4,blank=True,null=True)
    trailer=models.CharField(max_length=100)
    img1=models.ImageField(verbose_name="Subir Imagen 1",blank=True,null=True)
    img2=models.ImageField(verbose_name="Subir Imagen 2",blank=True,null=True)
    img3=models.ImageField(verbose_name="Subir Imagen 3",blank=True,null=True)
    img4=models.ImageField(verbose_name="Subir Imagen 4",blank=True,null=True)
    enlacegd=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Google Drive")
    enlacegd2=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Google Drive 2")
    enlacegd3=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Google Drive 3")
    enlacegd4=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Google Drive 4")
    enlacegd5=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Google Drive 5")
    enlacesub=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Subtitulo")
    enlacemg=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Mega ")
    enlacemg2=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Mega 2")
    enlacemg3=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Mega 3")
    enlacemg4=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Mega 4")
    enlacemg5=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Mega 5")
    comparte=models.CharField(max_length=500,blank=True,null=True)
    enlace_publi=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace publicidad")
    enlace_publi2=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace publicidad")
    enlace_publi3=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace publicidad")
    enlace_publi4=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace publicidad")
    enlace_publi5=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace publicidad")
    class Meta:
        ordering = ['id',]
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('cursos', kwargs={'slug': self.slug_curso})
def slug_generator_curso(sender,instance,*args,**kwargs):
    if instance.slug_curso:
        return
    instance.slug_curso=slugify(instance.nombre)
pre_save.connect(slug_generator_curso,sender=cursos)

def only_year_curso(sender,instance,*args,**kwargs):
    if instance.anio:
        return
    instance.anio=instance.fecha_estreno.year
pre_save.connect(only_year_curso,sender=cursos)       

class cupones(models.Model):
    nombre=models.CharField(max_length=250,verbose_name="Nombre:")
    nombre_original=models.CharField(max_length=250,verbose_name="Nombre Original:")
    slug_cupon=models.SlugField(max_length=250,null=True,blank=True)
    descripcion=models.CharField(max_length=1000,verbose_name="Descripcion:")
    plataforma=models.ForeignKey(plataforma_cursos,on_delete=models.CASCADE,verbose_name="Indicar la Plataforma de Cursos:")
    genero=models.ManyToManyField(categorias_cursos,verbose_name="Generios Cursos:")
    lenguaje=models.ManyToManyField(lenguaje_cursos,verbose_name="Lenguaje Cursos:",null=True,blank=True)
    Author=models.CharField(max_length=150)
    calificacion=models.CharField(max_length=100)
    descargas=models.IntegerField()
    idiomas=models.CharField(max_length=150,choices=idioma,null=True,blank=True,default=idioma[0])
    fecha_estreno=models.DateField(verbose_name="Fecha del Curso")
    fecha_subida=models.DateField(verbose_name="Fecha de Subida",auto_now_add=True)
    anio=models.CharField(max_length=4,blank=True,null=True)
    trailer=models.CharField(max_length=100)
    img1=models.ImageField(verbose_name="Subir Imagen 1",blank=True,null=True)
    img2=models.ImageField(verbose_name="Subir Imagen 2",blank=True,null=True)
    img3=models.ImageField(verbose_name="Subir Imagen 3",blank=True,null=True)
    img4=models.ImageField(verbose_name="Subir Imagen 4",blank=True,null=True)
    enlacegd=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Google Drive")
    enlacegd2=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Google Drive 2")
    enlace_publi=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace publicidad")
    enlace_publi2=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace publicidad2")
    class Meta:
        ordering = ['id',]
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('cursos', kwargs={'slug': self.slug_cupon})
def slug_generator_cupon(sender,instance,*args,**kwargs):
    if instance.slug_cupon:
        return
    instance.slug_cupon=slugify(instance.nombre)
pre_save.connect(slug_generator_cupon,sender=cupones)

def only_year_cupon(sender,instance,*args,**kwargs):
    if instance.anio:
        return
    instance.anio=instance.fecha_estreno.year
pre_save.connect(only_year_cupon,sender=cupones)

class articulos(models.Model):
    nombre=models.CharField(max_length=250,verbose_name="Nombre:")
    nombre_original=models.CharField(max_length=250,verbose_name="Nombre Original:")
    slug_articulo=models.SlugField(max_length=250,null=True,blank=True)
    descripcion=models.CharField(max_length=1000,verbose_name="Descripcion:")
    plataforma=models.ForeignKey(plataforma_cursos,on_delete=models.CASCADE,verbose_name="Indicar la Plataforma de Cursos:")
    genero=models.ManyToManyField(categorias_cursos,verbose_name="Generios Cursos:")
    lenguaje=models.ManyToManyField(lenguaje_cursos,verbose_name="Lenguaje Cursos:",null=True,blank=True)
    Author=models.CharField(max_length=150)
    calificacion=models.CharField(max_length=100)
    descargas=models.IntegerField()
    idiomas=models.CharField(max_length=150,choices=idioma,null=True,blank=True,default=idioma[0])
    fecha_estreno=models.DateField(verbose_name="Fecha del Curso")
    fecha_subida=models.DateField(verbose_name="Fecha de Subida",auto_now_add=True)
    anio=models.CharField(max_length=4,blank=True,null=True)
    trailer=models.CharField(max_length=100)
    img1=models.ImageField(verbose_name="Subir Imagen 1",blank=True,null=True)
    img2=models.ImageField(verbose_name="Subir Imagen 2",blank=True,null=True)
    img3=models.ImageField(verbose_name="Subir Imagen 3",blank=True,null=True)
    img4=models.ImageField(verbose_name="Subir Imagen 4",blank=True,null=True)
    enlacegd=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Google Drive")
    enlacegd2=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace Google Drive 2")
    enlace_publi=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace publicidad")
    enlace_publi2=models.CharField(max_length=500,blank=True,null=True,verbose_name="Enlace publicidad2")
    class Meta:
        ordering = ['id',]
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('cursos', kwargs={'slug': self.slug_articulo})
def slug_generator_articulo(sender,instance,*args,**kwargs):
    if instance.slug_articulo:
        return
    instance.slug_articulo=slugify(instance.nombre)
pre_save.connect(slug_generator_articulo,sender=articulos)

def only_year_articulos(sender,instance,*args,**kwargs):
    if instance.anio:
        return
    instance.anio=instance.fecha_estreno.year
pre_save.connect(only_year_articulos,sender=articulos)

