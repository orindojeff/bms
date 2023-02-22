from django.urls import path
from . import views
from .views import *

app_name = 'inventory'

urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category-list/', CategoryListView.as_view(), name='category-list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('payment/<int:pk>/', views.PaymentDetailView.as_view(), name='payment-detail'),
    path('payment/create/', views.PaymentCreateView.as_view(), name='payment-create'),
    path('payment/<int:pk>/update/', views.PaymentUpdateView.as_view(), name='payment-update'),
    path('payment/<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='payment-delete'),



    # # cart
    # path('view-product', views.ProductView.as_view(), name='view-product'),
    # path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/', cart, name='cart'),
    # path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    # path('decrease_cart_item/<int:product_id>/', decrease_cart_item, name='decrease_cart_item'),
    # path('checkout/', checkout, name='checkout'),
]
