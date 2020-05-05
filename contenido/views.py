from django.shortcuts import render,get_object_or_404,redirect
from .models import peliculas,categorias
from django.views.defaults import page_not_found
from random import randint
# Create your views here.
categoria_genero=categorias.objects.get_queryset().order_by('nombre')
anio_film=peliculas.objects.values_list('anio',flat=True).distinct().order_by('-anio')
pocos_requisitos=peliculas.objects.all()[8:16]
medios_requisitos=peliculas.objects.all()[16:24]
altos_requisitos=peliculas.objects.all()[24:31]
mas_visitados=peliculas.objects.all()[15:23]
mas_descargados=peliculas.objects.all()[:8]
last_film_add=peliculas.objects.get_queryset().order_by('-id')[:8]

def mi_error_404(request,exception):
    return page_not_found(request,exception,template_name="404.html")
def robots(request):
    return render(request,"robots.txt", content_type="text/plain")
def principal(request):
    recomend_film1=peliculas.objects.filter(id=81)
    recomend_film2=peliculas.objects.filter(id=89)
    recomend_film3=peliculas.objects.filter(id=118)
    recomend_film4=peliculas.objects.filter(id=8)
    recomend_film5=peliculas.objects.filter(id=9)
    recomend_film6=peliculas.objects.filter(id=3)
    #all_data=[]
    pelicula=peliculas.objects.all()
    categorias_slug=categorias.objects.values_list('slug_categoria',flat=True).distinct().order_by('nombre')
    #for categoria in categorias_slug:
    #    current_data={}
    #    current_fil=[]
    #    current_fil.append(peliculas.objects.filter(genero__slug_categoria=categoria))
    #    current_data['genero']=categoria
    #    current_data['pelicula']=current_fil
    #    all_data.append(current_data)
    data={
        'peliculas':pelicula,
        'pocos_requisitos':pocos_requisitos,
        'medios_requisitos':medios_requisitos,
        'altos_requisitos':altos_requisitos,
        'mas_visitados':mas_visitados,
        'mas_descargados':mas_descargados,
        'last_film_add':last_film_add,
        'categoria_genero':categoria_genero,
        'anio_film':anio_film,
        'recomend_film1':recomend_film1,
        'recomend_film2':recomend_film2,
        'recomend_film3':recomend_film3,
        'recomend_film4':recomend_film4,
        'recomend_film5':recomend_film5,
        'recomend_film6':recomend_film6,
    }
    return render(request,"principal.html",data)

def pelicula(request,slug):
    pelicula=get_object_or_404(peliculas,slug_peliculas=slug)
    count=peliculas.objects.count()
    recomendacion1=peliculas.objects.all()[randint(0,count-1)]
    recomendacion2=peliculas.objects.all()[randint(0,count-1)]
    recomendacion3=peliculas.objects.all()[randint(0,count-1)]
    recomendacion4=peliculas.objects.all()[randint(0,count-1)]
    recomendacion5=peliculas.objects.all()[randint(0,count-1)]
    recomendacion6=peliculas.objects.all()[randint(0,count-1)]
    recomendacion7=peliculas.objects.all()[randint(0,count-1)]
    recomendacion8=peliculas.objects.all()[randint(0,count-1)]
    recomendacion9=peliculas.objects.all()[randint(0,count-1)]
    recomendacion10=peliculas.objects.all()[randint(0,count-1)]
    data={
        'pelicula':pelicula,
        'recomendacion1':recomendacion1,
        'recomendacion2':recomendacion2,
        'recomendacion3':recomendacion3,
        'recomendacion4':recomendacion4,
        'recomendacion5':recomendacion5,
        'recomendacion6':recomendacion6,
        'recomendacion7':recomendacion7,
        'recomendacion8':recomendacion8,
        'recomendacion9':recomendacion9,
        'recomendacion10':recomendacion10,

      
    }
    return render(request,"pelicula.html",data)
def series(request,slug):
    pelicula=get_object_or_404(peliculas,slug_peliculas=slug)
    count=peliculas.objects.count()
    recomendacion1=peliculas.objects.all()[randint(0,count-1)]
    recomendacion2=peliculas.objects.all()[randint(0,count-1)]
    recomendacion3=peliculas.objects.all()[randint(0,count-1)]
    recomendacion4=peliculas.objects.all()[randint(0,count-1)]
    recomendacion5=peliculas.objects.all()[randint(0,count-1)]
    recomendacion6=peliculas.objects.all()[randint(0,count-1)]
    recomendacion7=peliculas.objects.all()[randint(0,count-1)]
    recomendacion8=peliculas.objects.all()[randint(0,count-1)]
    recomendacion9=peliculas.objects.all()[randint(0,count-1)]
    recomendacion10=peliculas.objects.all()[randint(0,count-1)]
    data={
        'pelicula':pelicula,
        'recomendacion1':recomendacion1,
        'recomendacion2':recomendacion2,
        'recomendacion3':recomendacion3,
        'recomendacion4':recomendacion4,
        'recomendacion5':recomendacion5,
        'recomendacion6':recomendacion6,
        'recomendacion7':recomendacion7,
        'recomendacion8':recomendacion8,
        'recomendacion9':recomendacion9,
        'recomendacion10':recomendacion10,

      
    }
    return render(request,"series.html",data)

def pelicula_genero(request,slug):
    pelicula=peliculas.objects.filter(genero__slug_categoria=slug)
    categoria_genero=categorias.objects.get_queryset().order_by('nombre')
    genero=slug
    if pelicula.exists():
        data={
        'peliculas':pelicula,
        'pocos_requisitos':pocos_requisitos,
        'medios_requisitos':medios_requisitos,
        'altos_requisitos':altos_requisitos,
        'mas_visitados':mas_visitados,
        'mas_descargados':mas_descargados,
        'last_film_add':last_film_add,
        'categoria_genero':categoria_genero,
        'anio_film':anio_film,
        'genero':genero,
        }
        return render(request,"peliculas_categorias.html",data)
    else:
        return redirect('principal')
def pelicula_anio(request,slug):
    pelicula=peliculas.objects.filter(anio=slug)
    if pelicula.exists():
        data={
        'peliculas':pelicula,
        'pocos_requisitos':pocos_requisitos,
        'medios_requisitos':medios_requisitos,
        'altos_requisitos':altos_requisitos,
        'mas_visitados':mas_visitados,
        'mas_descargados':mas_descargados,
        'last_film_add':last_film_add,
        'categoria_genero':categoria_genero,
        'anio_film':anio_film,
        }
        return render(request,"peliculas_anio.html",data)
    else:
        return redirect('principal')