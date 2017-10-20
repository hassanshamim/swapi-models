from django.contrib import admin
from api import models

from django.http import HttpResponse
from django.core import serializers


# Register your models here.

class PlanetAdmin(admin.ModelAdmin):
    list_display = ['name', 'population', 'has_enough_water']
    list_filter = ['gravity', 'surface_water']
    # fields = ['name', 'population']

    actions = ['export_as_json']

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response

    def has_enough_water(self, obj):
        water = obj.surface_water
        if not water.isdigit():
            return False
        return int(water) > 10
    has_enough_water.short_description = 'Habitable?'
    has_enough_water.boolean = True



admin.site.register(models.Planet, PlanetAdmin)

admin.site.register(models.People)
admin.site.register(models.Species)
admin.site.register(models.Vehicle)
admin.site.register(models.Transport)
admin.site.register(models.Starship)
admin.site.register(models.Film)
