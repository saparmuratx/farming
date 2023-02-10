from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import (
    Farmer,
    Culture,
    Season,
    Plot,
)


admin.site.register(Farmer)
admin.site.register(Culture)
admin.site.register(Season)


@admin.register(Plot)
class PlotAdmin(OSMGeoAdmin):
    list_display = ("contour", "farmer", "culture", "season")
