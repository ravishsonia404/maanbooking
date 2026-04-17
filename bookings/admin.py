from django.contrib import admin
from django.utils.html import format_html
from .models import Ride


class RideAdmin(admin.ModelAdmin):

    # 🔥 Columns shown in admin
    list_display = (
        'name',
        'pickup',
        'drop',
        'date',
        'time',
        'driver',
        'colored_status',
        'colored_price'
    )

    # 🔍 Filters (left sidebar)
    list_filter = ('status', 'date', 'driver')

    # 🔎 Search bar
    search_fields = ('name', 'pickup', 'drop', 'email')

    # ✏️ Editable fields directly
    list_editable = ('driver',)

    # 📅 Ordering
    ordering = ('-date',)

    # 🚦 Colored Status
    def colored_status(self, obj):
        if obj.status == 'pending':
            return format_html('<span style="color:orange; font-weight:bold;">Pending</span>')
        elif obj.status == 'accepted':
            return format_html('<span style="color:green; font-weight:bold;">Accepted</span>')
        elif obj.status == 'rejected':
            return format_html('<span style="color:red; font-weight:bold;">Rejected</span>')
        elif obj.status == 'completed':
            return format_html('<span style="color:blue; font-weight:bold;">Completed</span>')
        return obj.status

    colored_status.short_description = 'Status'

    # 💰 Colored Price
    def colored_price(self, obj):
        if obj.price:
            if obj.price > 200:
                return format_html('<b style="color:red;">₹{}</b>', obj.price)
            return format_html('<b style="color:green;">₹{}</b>', obj.price)
        return format_html('<span style="color:gray;">Not Set</span>')

    colored_price.short_description = 'Price'


admin.site.register(Ride, RideAdmin)
