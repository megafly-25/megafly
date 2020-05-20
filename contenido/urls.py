from django.urls import path
from django.conf.urls import handler404
from .views import principal,pelicula,robots,mi_error_404,pelicula_genero,pelicula_anio,serie,temporada_serie,verserie,principal_juegos,juegospc,juegos_anio,juegos_genero,juegopc,juegospsx,juegopsx,juegosps2,juegops2,juegosps3,juegops3
from django.contrib.sitemaps.views import sitemap
from contenido.sitemaps import PeliculasSitemap
sitemaps = {
    'peliculas': PeliculasSitemap,
}
urlpatterns = [
    path('',principal,name="principal"),
    path('pelicula/<slug>',pelicula,name="pelicula"),
    path('serie/<slug>',serie,name="serie"),
    path('<nombre>/<temporada_slug>/<slug>/',temporada_serie,name="temporada_serie"),
    path('<nombre>/capitulo-<capitulo>/<slug>',verserie,name="verserie"),
    path('peliculas/de/<slug>',pelicula_genero,name="pelicula_genero"),
    path('peliculas/del/<slug>',pelicula_anio,name="pelicula_anio"),
    path('juegos',principal_juegos,name="principal_juegos"),
    path('juego/de/pc/<slug>',juegopc,name="juegopc"),
    path('juegos-de-pc',juegospc,name="juegospc"),
    path('juego/de/psx/<slug>',juegopsx,name="juegopsx"),
    path('juegos-de-psx',juegospsx,name="juegospsx"),
    path('juego/de/ps2/<slug>',juegops2,name="juegops2"),
    path('juegos-de-ps2',juegosps2,name="juegosps2"),
    path('juego/de/ps3/<slug>',juegops3,name="juegops3"),
    path('juegos-de-ps3',juegosps3,name="juegosps3"),
    #path('juegos/de/<slug>',juegos_genero,name="juegos_genero"),
    #path('juegos/del/<slug>',juegos_anio,name="juegos_anio"),
    path('robots.txt',robots),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

handler404=mi_error_404