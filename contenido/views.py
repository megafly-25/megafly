from django.shortcuts import render,get_object_or_404,redirect
from .models import series,peliculas,categorias,temporadas,categorias,ntemporada,capitulos,gamespc,gamespsx,gamesps2,gamesps3
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
    serie=series.objects.all()
    #all_data=[]
    pelicula=peliculas.objects.all()
    #categorias_slug=categorias.objects.values_list('slug_categoria',flat=True).distinct().order_by('nombre')
    
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
        'serie':serie,
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
def serie(request,slug):
    serie=get_object_or_404(series,slug_serie=slug)
    temporada=temporadas.objects.filter(serie=serie.id)
    ntemporadas=ntemporada.objects.all()
    count=series.objects.count()
    recomendacion1=series.objects.all()[randint(0,count-1)]
    data={
        'pelicula':pelicula,
        'recomendacion1':recomendacion1,
        'serie':serie,
        'temporada':temporada,
        'ntemporadas':ntemporadas,
    }
    return render(request,"series.html",data)
def temporada_serie(request,slug,nombre,temporada_slug):
    #temporada_serie=get_object_or_404(capitulos,temporada__slug_temporada=slug)
    temporada_serie=capitulos.objects.filter(temporada__slug_temporada=slug)
    ntemporadas=ntemporada.objects.filter(slug_ntemporada=temporada_slug)
    temporada=temporadas.objects.filter(slug_temporada=slug)
    all_series=series.objects.filter(slug_serie=nombre)
    count=series.objects.count()
    recomendacion1=peliculas.objects.all()[randint(0,count-1)]
    data={
        'pelicula':pelicula,
        'recomendacion1':recomendacion1,
        'all_series':all_series,
        'temporada_slug':temporada_slug,
        'temporada_serie':temporada_serie,
        'ntemporada':ntemporadas,
        'temporada':temporada,
    }
    return render(request,"temporadas_serie.html",data)
def verserie(request,slug,nombre,capitulo):
    verseries=capitulos.objects.filter(slug_capitulo=slug)
    count=peliculas.objects.count()
    recomendacion1=peliculas.objects.all()[randint(0,count-1)]
    data={
        'recomendacion1':recomendacion1, 
        'verseries':verseries,
        'nombre':nombre,
        'capitulo':capitulo,
    }
    return render(request,"ver_serie.html",data)
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
def principal_juegos(request):
    juegospc=gamespc.objects.all()
    juegospsx=gamespsx.objects.all()
    juegosps2=gamesps2.objects.all()
    juegosps3=gamesps3.objects.all()
    last_film_add=peliculas.objects.get_queryset().order_by('-id')[:8]
    last_serie_add=series.objects.get_queryset().order_by('-id')[:8]
    data={
        'juegospc':juegospc,
        'juegospsx':juegospsx,
        'juegosps2':juegosps2,
        'juegosps3':juegosps3,
        'last_film_add':last_film_add,
        'last_serie_add':last_serie_add,
        
    }
    return render(request,"principal_juegos.html",data)
def juegos_genero(request,slug):
    juegospc=gamespc.objects.filter(genero__slug_categoria=slug)
    juegospsx=gamespsx.objects.filter(genero__slug_categoria=slug)
    juegosps2=gamesps2.objects.filter(genero__slug_categoria=slug)
    juegosps3=gamesps3.objects.filter(genero__slug_categoria=slug)
    pocos_requisitos=gamespc.objects.all()[8:16]
    medios_requisitos=gamespc.objects.all()[16:24]
    altos_requisitos=gamespc.objects.all()[24:31]
    mas_visitados=gamespc.objects.all()[15:23]
    mas_descargados=gamespc.objects.all()[:8]
    last_film_add=peliculas.objects.get_queryset().order_by('-id')[:8]
    last_serie_add=series.objects.get_queryset().order_by('-id')[:8]
    genero=slug
    if juegospc.exists():
        data={
        'juegospc':juegospc,
        'juegospsx':juegospsx,
        'juegosps2':juegosps2,
        'juegosps3':juegosps3,
        'pocos_requisitos':pocos_requisitos,
        'medios_requisitos':medios_requisitos,
        'altos_requisitos':altos_requisitos,
        'mas_visitados':mas_visitados,
        'mas_descargados':mas_descargados,
       'last_film_add':last_film_add,
        'last_serie_add':last_serie_add,
        'categoria_genero':categoria_genero,
        'anio_film':anio_film,
        'genero':genero,
        }
        return render(request,"juegos_categorias.html",data)
    else:
        return redirect('principal')
def juegos_anio(request,slug):
    juegospc=gamespc.objects.filter(genero__slug_categoria=slug)
    juegospsx=gamespsx.objects.filter(genero__slug_categoria=slug)
    juegosps2=gamesps2.objects.filter(genero__slug_categoria=slug)
    juegosps3=gamesps3.objects.filter(genero__slug_categoria=slug)
    pocos_requisitos=gamespc.objects.all()[8:16]
    medios_requisitos=gamespc.objects.all()[16:24]
    altos_requisitos=gamespc.objects.all()[24:31]
    mas_visitados=gamespc.objects.all()[15:23]
    mas_descargados=gamespc.objects.all()[:8]
    last_film_add=peliculas.objects.get_queryset().order_by('-id')[:8]
    last_serie_add=series.objects.get_queryset().order_by('-id')[:8]
    if juegospc.exists():
        data={
        'juegospc':juegospc,
        'juegospsx':juegospsx,
        'juegosps2':juegosps2,
        'juegosps3':juegosps3,
        'pocos_requisitos':pocos_requisitos,
        'medios_requisitos':medios_requisitos,
        'altos_requisitos':altos_requisitos,
        'mas_visitados':mas_visitados,
        'mas_descargados':mas_descargados,
        'last_film_add':last_film_add,
        'last_serie_add':last_serie_add,
        'categoria_genero':categoria_genero,
        'anio_film':anio_film,
        }
        return render(request,"juegos_anio.html",data)
    else:
        return redirect('principal')
def juegospc(request):
    juegospc=gamespc.objects.all()
    pocos_requisitos=gamespc.objects.all()[8:16]
    medios_requisitos=gamespc.objects.all()[16:24]
    altos_requisitos=gamespc.objects.all()[24:31]
    mas_visitados=gamespc.objects.all()[15:23]
    mas_descargados=gamespc.objects.all()[:8]
    last_film_add=peliculas.objects.get_queryset().order_by('-id')[:8]
    last_serie_add=series.objects.get_queryset().order_by('-id')[:8]
    data={
        'juegospc':juegospc,
        'pocos_requisitos':pocos_requisitos,
        'medios_requisitos':medios_requisitos,
        'altos_requisitos':altos_requisitos,
        'mas_visitados':mas_visitados,
        'mas_descargados':mas_descargados,
        'last_film_add':last_film_add,
        'last_serie_add':last_serie_add,
        'categoria_genero':categoria_genero,
        'anio_film':anio_film,
    }
    return render(request,"juegospc.html",data)
def juegopc(request,slug):
    juego=get_object_or_404(gamespc,slug_gamespc=slug)
    count=gamespc.objects.count()
    recomendacion1=gamespc.objects.all()[randint(0,count-1)]
    data={
        'juego':juego,
        'recomendacion1':recomendacion1,
        
    }
    return render(request,"juegopc.html",data)
def juegospsx(request):
    juegospsx=gamespsx.objects.all()
    pocos_requisitos=gamespsx.objects.all()[8:16]
    medios_requisitos=gamespsx.objects.all()[16:24]
    altos_requisitos=gamespsx.objects.all()[24:31]
    mas_visitados=gamespsx.objects.all()[15:23]
    mas_descargados=gamespsx.objects.all()[:8]
    last_film_add=peliculas.objects.get_queryset().order_by('-id')[:8]
    last_serie_add=series.objects.get_queryset().order_by('-id')[:8]
    data={
        'juegospsx':juegospsx,
        'pocos_requisitos':pocos_requisitos,
        'medios_requisitos':medios_requisitos,
        'altos_requisitos':altos_requisitos,
        'mas_visitados':mas_visitados,
        'mas_descargados':mas_descargados,
        'last_film_add':last_film_add,
        'last_serie_add':last_serie_add,
        'categoria_genero':categoria_genero,
        'anio_film':anio_film,
    }
    return render(request,"juegospsx.html",data)
def juegopsx(request,slug):
    juego=get_object_or_404(gamespsx,slug_gamespsx=slug)
    count=gamespsx.objects.count()
    recomendacion1=gamespsx.objects.all()[randint(0,count-1)]
    data={
        'juego':juego,
        'recomendacion1':recomendacion1,
        
    }
    return render(request,"juegopsx.html",data)
def juegosps2(request):
    juegosps2=gamesps2.objects.all()
    pocos_requisitos=gamesps2.objects.all()[8:16]
    medios_requisitos=gamesps2.objects.all()[16:24]
    altos_requisitos=gamesps2.objects.all()[24:31]
    mas_visitados=gamesps2.objects.all()[15:23]
    mas_descargados=gamesps2.objects.all()[:8]
    last_film_add=peliculas.objects.get_queryset().order_by('-id')[:8]
    last_serie_add=series.objects.get_queryset().order_by('-id')[:8]
    data={
        'juegosps2':juegosps2,
        'pocos_requisitos':pocos_requisitos,
        'medios_requisitos':medios_requisitos,
        'altos_requisitos':altos_requisitos,
        'mas_visitados':mas_visitados,
        'mas_descargados':mas_descargados,
        'last_film_add':last_film_add,
        'last_serie_add':last_serie_add,
        'categoria_genero':categoria_genero,
        'anio_film':anio_film,
    }
    return render(request,"juegosps2.html",data)
def juegops2(request,slug):
    juego=get_object_or_404(gamesps2,slug_gamesps2=slug)
    count=gamesps2.objects.count()
    recomendacion1=gamesps2.objects.all()[randint(0,count-1)]
    data={
        'juego':juego,
        'recomendacion1':recomendacion1,
        
    }
    return render(request,"juegops2.html",data)

def juegosps3(request):
    juegosps3=gamesps3.objects.all()
    pocos_requisitos=gamesps3.objects.all()[8:16]
    medios_requisitos=gamesps3.objects.all()[16:24]
    altos_requisitos=gamesps3.objects.all()[24:31]
    mas_visitados=gamesps3.objects.all()[15:23]
    mas_descargados=gamesps3.objects.all()[:8]
    last_film_add=peliculas.objects.get_queryset().order_by('-id')[:8]
    last_serie_add=series.objects.get_queryset().order_by('-id')[:8]
    data={
        'juegosps3':juegosps3,
        'pocos_requisitos':pocos_requisitos,
        'medios_requisitos':medios_requisitos,
        'altos_requisitos':altos_requisitos,
        'mas_visitados':mas_visitados,
        'mas_descargados':mas_descargados,
        'last_film_add':last_film_add,
        'last_serie_add':last_serie_add,
        'categoria_genero':categoria_genero,
        'anio_film':anio_film,
    }
    return render(request,"juegosps3.html",data)
def juegops3(request,slug):
    juego=get_object_or_404(gamesps3,slug_gamesps3=slug)
    count=gamesps3.objects.count()
    recomendacion1=gamesps3.objects.all()[randint(0,count-1)]
    data={
        'juego':juego,
        'recomendacion1':recomendacion1,
        
    }
    return render(request,"juegops3.html",data)