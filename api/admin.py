from django.contrib import admin
from api import models

# Register your models here.
admin.site.register(models.Vehicle)
admin.site.register(models.Transport)
admin.site.register(models.Starship)
admin.site.register(models.Film)
