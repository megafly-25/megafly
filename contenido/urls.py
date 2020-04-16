from django.urls import path
from django.conf.urls import handler404
from .views import principal,pelicula,robots,mi_error_404
from django.contrib.sitemaps.views import sitemap
from contenido.sitemaps import PeliculasSitemap
sitemaps = {
    'peliculas': PeliculasSitemap,
}
urlpatterns = [
    path('',principal,name="principal"),
    path('peliculas/<slug>',pelicula,name="pelicula"),
    path('robots.txt',robots),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

handler404=mi_error_404