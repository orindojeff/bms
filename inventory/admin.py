from django.contrib import admin
from django.contrib import admin
from .models import Product, Category, Service, Order, OrderItem
from django.contrib.auth.models import Group
from django.utils.html import format_html
from moneyed import Money


admin.site.unregister(Group)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'installation_cost', 'total_cost', 'image', 'created_at', 'updated_at')
    list_filter = ('name', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    search_fields = ('name', 'description', 'category')

    def total_cost(self, obj):
        return obj.total_cost


    def installation_cost(self, obj):
         return obj.category.installation_cost

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'installation_cost',)
    ordering = ('name',)
    search_fields = ('name',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    ordering = ()
    search_fields = ('name',)





class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'service', 'quantity',)
    list_filter = ('product',)
    search_fields = ('product', 'order')
    readonly_fields = ()

    def service(self, obj):
        return obj.order.service
    


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'date_ordered', 'service_cost_display', 'is_completed')
    list_filter = ('service', 'is_completed')
    search_fields = ('id', 'user__username')
    readonly_fields = ('service_cost',)

    def service_cost_display(self, obj):
        return obj.service_cost
        

    service_cost_display.short_description = 'Service Cost'

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Product, ProductAdmin,)
admin.site.register(Category, CategoryAdmin,)
admin.site.register(Service, ServiceAdmin,)