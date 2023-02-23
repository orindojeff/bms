from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import CategoryForm, ProductForm, OrderForm,PaymentForm
from .models import Category, Product, Order, Payment
from django.views.generic import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product,Order, CartItem, Cart
from .forms import AddToCartForm
from .utils import get_or_create_order, get_or_create_order_id, get_or_create_cart
from django.db.models import Sum
from django.db import transaction
from django.urls import reverse


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'inventory/includes/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(LoginRequiredMixin,  CreateView):
    model = Category
    template_name = 'inventory/includes/create_category.html'
    form_class = CategoryForm

    def test_func(self):
        return self.request.user.is_superuser

class CategoryUpdateView(LoginRequiredMixin,  UpdateView):
    model = Category
    template_name = 'inventory/includes/category_update_form.html'
    form_class = CategoryForm

    def test_func(self):
        return self.request.user.is_superuser

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category-list')


def Category(request):
    category = Category.objects.all()
    return render (request,  {'category': category})

    def test_func(self):
        return self.request.user.is_superuser

class ProductListView(ListView):
    model = Product
    template_name = 'inventory/includes/product_list.html'
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'inventory/includes/product_form.html'
    form_class = ProductForm

    def test_func(self):
        return self.request.user.is_superuser

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'inventory/includes/product_update_form.html'
    form_class = ProductForm

    def test_func(self):
        return self.request.user.is_superuser

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'inventory/includes/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

    def test_func(self):
        return self.request.user.is_superuser


class ProductDetailView(DetailView):
    model = Product
    template_name = 'inventory/includes/product_detail.html'
    context_object_name = 'product'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_form.html'
    form_class = OrderForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Order
    template_name = 'order_detail.html'

    def test_func(self):
        return self.get_object().user == self.request.user

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'inventory/includes/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def order_quantity(self, obj):
        return obj.orderitem.quantity


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_list = self.get_queryset()
        order_data = []
        for order in order_list:
            transaction_id = order.transaction_id
            order_data.append({
                'order': order,
                'transaction_id': transaction_id
            })
        context['order_data'] = order_data
        return context



    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

def order(request):
    order = Order.objects.all()
    return render (request,  {'order': order})

class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    template_name = 'order_form.html'
    form_class = OrderForm

    def test_func(self):
        return self.get_object().user == self.request.user



class PaymentCreateView(CreateView):
    model = Payment
    template_name = 'payment_form.html'
    form_class = PaymentForm

    def form_valid(self, form):
        form.instance.order = self.request.GET.get('order')
        return super().form_valid(form)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order-list')

    def test_func(self):
        return self.get_object().user == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Order deleted successfully.")
        return super().delete(request, *args, **kwargs)


class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment_detail.html'
    context_object_name = 'payment'


class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment_form.html'
    context_object_name = 'payment'

    def get_success_url(self):
        return reverse('payment-detail', kwargs={'pk': self.object.pk})


class PaymentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Payment
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('payment-list')

    def test_func(self):
        return self.get_object().order.user == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Payment deleted successfully.")
        return super().delete(request, *args, **kwargs)



# def order_detail(request, order_id):
#     order = get_object_or_404(Order, pk=order_id)
#     order_items = OrderItem.objects.filter(order=order)
#     for item in order_items:
#         item.quantity_ordered = item.quantity
#         # get the quantity of the product in the order
#         item.quantity_in_order = OrderItem.objects.filter(order_id=order.id, product_id=item.product.id).aggregate(Sum('quantity'))['quantity__sum']
#     context = {
#         'order': order,
#         'order_items': order_items,
#     }
#     return render(request, 'orders/order_detail.html', context)


class ProductView(ListView):
    model = Product
    template_name = 'customer/view-product.html'
    context_object_name = 'products'
    paginate_by = 12


