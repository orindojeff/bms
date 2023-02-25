from django.urls import path
from .views import (
    OrderCreateView, OrderUpdateView, OrderDeleteView, OrderListView,
    SalesCreateView, SalesUpdateView, SalesDeleteView, SalesListView,
    PaymentCreateView, PaymentUpdateView, PaymentDeleteView, PaymentListView, index,
)


app_name = 'inventory'

urlpatterns = [
    path('', index, name='index'),
    # Order URLs
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('orders/', OrderListView.as_view(), name='order-list'),

    # Sales URLs
    path('sales/create/', SalesCreateView.as_view(), name='sales-create'),
    path('sales/<int:pk>/update/', SalesUpdateView.as_view(), name='sales-update'),
    path('sales/<int:pk>/delete/', SalesDeleteView.as_view(), name='sales-delete'),
    path('sales/', SalesListView.as_view(), name='sales-list'),

    # Payment URLs
    path('payments/create/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<int:pk>/update/', PaymentUpdateView.as_view(), name='payment-update'),
    path('payments/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment-delete'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),

     
]
