from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import School


class SchoolAdmin(LeafletGeoAdmin):
    list_display = ['name', 'regional', 'level', 'governance']

    
admin.site.register(School, SchoolAdmin)
