from django.contrib import admin, messages
from django.contrib.admin import ModelAdmin
from .models import Location, PickUpStation, UserPickUpStation, Delivery


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at',)


class PickUpStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at', 'updated_at',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at',)


class UserPickUpStationAdmin(admin.ModelAdmin):
    list_display = ('user', 'station', 'created_at', 'updated_at',)
    list_filter = ('created_at', 'updated_at', 'station')
    search_fields = ('user', 'station',)
    readonly_fields = ('created_at', 'updated_at',)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'delivery_date', 'station', 'status', 'driver',)
    list_filter = ('delivery_date', 'station',)
    search_fields = ('name', 'order')
    readonly_fields = ('delivery_date',)


admin.site.register(Location, LocationAdmin)
admin.site.register(PickUpStation, PickUpStationAdmin)
admin.site.register(UserPickUpStation, UserPickUpStationAdmin)
admin.site.register(Delivery, DeliveryAdmin)
