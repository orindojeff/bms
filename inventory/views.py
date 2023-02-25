from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Order, Sales, Payment
from .forms import OrderForm, SalesForm, PaymentForm
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# Create views for Order model
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form.html'
    success_url = reverse_lazy('inventory:order-list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_update.html'
    success_url = reverse_lazy('inventory:order-list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('inventory:order-list')

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = context['object_list']
        paginator = Paginator(object_list, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)

        context['object_list'] = objects
        return context


# Create views for Sales model
class SalesCreateView(CreateView):
    model = Sales
    form_class = SalesForm
    template_name = 'sales_form.html'
    success_url = reverse_lazy('inventory:sales-list')

class SalesUpdateView(UpdateView):
    model = Sales
    form_class = SalesForm
    template_name = 'sales_update.html'
    success_url = reverse_lazy('inventory:sales-list')

class SalesDeleteView(DeleteView):
    model = Sales
    template_name = 'sales_confirm_delete.html'
    success_url = reverse_lazy('inventory:sales-list')

class SalesListView(ListView):
    model = Sales
    template_name = 'sales_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = context['object_list']
        paginator = Paginator(object_list, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)

        context['object_list'] = objects
        return context



# Create views for Payment model
class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment_form.html'
    success_url = reverse_lazy('inventory:payment-list')

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment_update.html'
    success_url = reverse_lazy('stock:payment-list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('inventory:payment-list')

class PaymentListView(ListView):
    model = Payment
    template_name = 'payment_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = context['object_list']
        paginator = Paginator(object_list, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)

        context['object_list'] = objects
        return context



def index(request):
    return render(request, 'index.html')





from django.core.paginator import Paginator
from django.views.generic import TemplateView

class PaginationView(TemplateView):
    template_name = 'pagination.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context

    def get_queryset(self):
        # Define the queryset to paginate
        # e.g. return MyModel.objects.all()
        raise NotImplementedError("Please define the 'get_queryset' method in your view.")
