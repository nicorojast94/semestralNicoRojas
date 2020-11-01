from django.contrib import admin
from .models import SliderIndex,Insumos,MisionyVision,Galeria
# Register your models here.

class InsumosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio','descripcion','stock']
    search_fields = ['nombre','descripcion']
    list_per_page = 10
class SlideIndexAdmin(admin.ModelAdmin):
    list_display = ['ident','imagen']
    search_fields = ['ident']
    list_per_page = 10
class MisionyVsionAdmin(admin.ModelAdmin):
    list_display = ['ident','mision','vision']
    search_fields = ['ident',]
    list_per_page = 10

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['ident','imagen']
    search_fields = ['ident']
    list_per_page = 10

admin.site.register(SliderIndex,SlideIndexAdmin)
admin.site.register(Insumos, InsumosAdmin)
admin.site.register(MisionyVision,MisionyVsionAdmin)
admin.site.register(Galeria,GaleriaAdmin)

