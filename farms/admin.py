from django.contrib import admin

from .models import (
    Farmer,
    Culture,
    Season,
)


admin.site.register(Farmer)
admin.site.register(Culture)
admin.site.register(Season)
