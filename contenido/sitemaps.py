from django.contrib.sitemaps import Sitemap
from .models import peliculas


class PeliculasSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return peliculas.objects.all()