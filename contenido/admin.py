from django.contrib import admin
from .models import categorias,gamespc,gamespsx,gamesps2,gamesps3,peliculas,series
# Register your models here.
class PeliculaAdmin(admin.ModelAdmin):
    list_display=['nombre','fecha_estreno','online','disco']
    search_fields=['nombre','nombre_original','descripcion','region','anio','fecha_subida','director','reparto','online']
    list_filter=['genero']
class CategoriaAdmin(admin.ModelAdmin):
    def get_queryset(self,request):
        queryset=super(CategoriaAdmin,self).get_queryset(request)
        queryset=queryset.order_by('nombre')
        return queryset
admin.site.register(categorias,CategoriaAdmin)
admin.site.register(gamespc)
admin.site.register(gamespsx)
admin.site.register(gamesps2)
admin.site.register(gamesps3)
admin.site.register(peliculas,PeliculaAdmin)
admin.site.register(series)
admin.site.site_header="Megafly Admin"
admin.site.index_title="Megafly Admin"
admin.site.site_title="Megafly Admin"
    