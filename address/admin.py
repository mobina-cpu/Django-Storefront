from django.contrib import admin
from .models import (
    State,
    City,
)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]
    search_fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'state'
    ]
    search_fields = ['name']
    list_filter = ['state']

