from django.contrib import admin, messages
from django.contrib.admin import ModelAdmin
from .models import OrderPayment, Invoice


# class OrderPaymentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'order', 'amount', 'transaction_id', 'date',)
#     list_filter = ('date',)
#     search_fields = ('transaction_id', 'order')
#     readonly_fields = ('date',)

# class InvoiceAdmin(admin.ModelAdmin):
#     list_display = ('invoice_number', 'order', 'customer', 'total_amount', 'date', 'payment_status',)
#     list_filter = ('date', 'payment_status',)
#     search_fields = ('customer', 'invoice_number')
#     readonly_fields = ('date',)

#     def payment_amount(self, obj):
#          return obj.order_payment.amount

#     def product_name(self, obj):
#         return obj.order.product.name

class OrderPaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user', 'amount', 'date',)
    list_filter = ('date',)
    search_fields = ('transaction_id', 'order')
    readonly_fields = ('date',)

    def user(self, obj):
        return obj.order.user

    # def o_id(self, obj):
    # #    return obj.order.transaction_id

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'order', 'customer', 'total_amount', 'date', 'payment_status',)
    list_filter = ('date', 'payment_status',)
    search_fields = ('customer', 'invoice_number')
    readonly_fields = ('date',)

    def order_name(self, obj):
        return obj.order.transaction_id

    def payment_amount(self, obj):
        return obj.order_payment.amount

    def product_name(self, obj):
        return obj.order.product.name






admin.site.register(OrderPayment, OrderPaymentAdmin)
admin.site.register(Invoice, InvoiceAdmin)
