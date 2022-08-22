from django.contrib import admin
from .models import Tee, Hoodies_Sweater, Pant, Exclusive_Apparel


class TeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'length', 'ptp', 'sold')
    search_fields = ['name']

class Hoodies_SweatersAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'length', 'ptp', 'sold')
    search_fields = ['name']

class PantsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'waist', 'inseam', 'rise', 'sold')
    search_fields = ['name']

class Exclusive_ApparelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'length', 'ptp', 'sold')
    search_fields = ['name']


# Register your models here.

admin.site.register(Tee, TeesAdmin)
admin.site.register(Hoodies_Sweater, Hoodies_SweatersAdmin)
admin.site.register(Pant, PantsAdmin)
admin.site.register(Exclusive_Apparel, Exclusive_ApparelAdmin)
