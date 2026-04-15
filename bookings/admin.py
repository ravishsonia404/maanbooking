from django.contrib import admin
from .models import Ride


class RideAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'pickup',
        'drop',
        'date',
        'price',
        'driver_name',
        'status'
    )

    list_filter = ('status', 'date', 'driver_name')
    search_fields = ('name', 'pickup', 'drop', 'driver_name')

    list_editable = ('price', 'driver_name', 'status')

    ordering = ('-id',)


admin.site.register(Ride, RideAdmin)