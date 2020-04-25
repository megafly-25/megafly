from django.urls import path
from django.conf.urls import handler404
from .views import principal,pelicula,robots,mi_error_404,pelicula_genero,pelicula_anio
from django.contrib.sitemaps.views import sitemap
from contenido.sitemaps import PeliculasSitemap
sitemaps = {
    'peliculas': PeliculasSitemap,
}
urlpatterns = [
    path('',principal,name="principal"),
    path('peliculas/<slug>',pelicula,name="pelicula"),
    path('peliculas/de/<slug>',pelicula_genero,name="pelicula_genero"),
    path('peliculas/del/<slug>',pelicula_anio,name="pelicula_anio"),
    path('robots.txt',robots),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

handler404=mi_error_404