from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Location, PickUpStation, UserPickUpStation, Shipping
from django.views.decorators.csrf import csrf_exempt
from .forms import LocationForm, PickUpStationForm, UserPickUpStationForm, ShippingForm


class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'location_form.html'
    success_url = reverse_lazy('shipping:location_list')


class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'location_form.html'
    success_url = reverse_lazy('shipping:location_list')


class LocationListView(ListView):
    model = Location
    template_name = 'location_list.html'
    context_object_name = 'locations'


class LocationDetailView(DetailView):
    model = Location
    template_name = 'location_detail.html'
    context_object_name = 'location'


class LocationDeleteView(DeleteView):
    model = Location
    template_name = 'location_delete.html'
    success_url = reverse_lazy('shipping:location_list')


class PickUpStationCreateView(CreateView):
    model = PickUpStation
    form_class = PickUpStationForm
    template_name = 'inventory/shipping/pickupstation_form.html'
    success_url = reverse_lazy('shipping:pickupstation_list')


class PickUpStationUpdateView(UpdateView):
    model = PickUpStation
    form_class = PickUpStationForm
    template_name = 'inventory/shipping/pickupstation_update.html'
    success_url = reverse_lazy('shipping:pickupstation_list')


class PickUpStationListView(ListView):
    model = PickUpStation
    template_name = 'inventory/shipping/pickupstation_list.html'
    context_object_name = 'pickupstations'


class PickUpStationDetailView(DetailView):
    model = PickUpStation
    template_name = 'inventory/shipping/pickupstation_detail.html'
    context_object_name = 'pickupstation'


class PickUpStationDeleteView(DeleteView):
    model = PickUpStation
    template_name = 'inventory/shipping/pickupstation_delete.html'
    success_url = reverse_lazy('shipping:pickupstation_list')


class UserPickUpStationCreateView(CreateView):
    model = UserPickUpStation
    form_class = UserPickUpStationForm
    template_name = 'userpickupstation_form.html'
    success_url = reverse_lazy('shipping:userpickupstation_list')


class UserPickUpStationUpdateView(UpdateView):
    model = UserPickUpStation
    form_class = UserPickUpStationForm
    template_name = 'userpickupstation_form.html'
    success_url = reverse_lazy('shipping:userpickupstation_list')


class UserPickUpStationListView(ListView):
    model = UserPickUpStation
    template_name = 'userpickupstation_list.html'
    context_object_name = 'userpickupstations'


class UserPickUpStationDetailView(DetailView):
    model = UserPickUpStation
    template_name = 'userpickupstation_detail.html'
    context_object_name = 'userpickupstation'


class UserPickUpStationDeleteView(DeleteView):
    model = UserPickUpStation
    template_name = 'userpickupstation_delete.html'
    success_url = reverse_lazy('shipping:userpickupstation_list')


class ShippingCreateView(CreateView):
    model = Shipping
    form_class = ShippingForm
    template_name = 'inventory/shipping/shipping_form.html'
    success_url = reverse_lazy('shipping:shipping_list')


class ShippingUpdateView(UpdateView):
    model = Shipping
    form_class = ShippingForm
    template_name = 'inventory/shipping/shipping_update.html'

class ShippingListView(ListView):
    model = Shipping
    template_name = 'inventory/shipping/shipping_list.html'
    context_object_name = 'shipping:shippings'


class ShippingDetailView(DetailView):
    model = Shipping
    template_name = 'inventory/shipping/shipping_detail.html'
    context_object_name = 'shipping:shipping'

def Shipping(request):
    shipping = Shipping.objects.all()
    return render (request,  {'Shipping': Shipping})




# generate all the advanced templates for the following views, app_name='Shipping', base='inventory/layouts/base.html
# LocationCreateView,
# LocationUpdateView
# LocationListView
# LocationDetailView
# LocationDeleteView
# PickUpStationCreateView
# PickUpStationUpdateView
# PickUpStationListView
# PickUpStationDetailView
#  PickUpStationDeleteView
# UserPickUpStationCreateView
#  UserPickUpStationUpdateView
# UserPickUpStationListView
# UserPickUpStationDetailView
# UserPickUpStationDeleteView
# ShippingCreateView
#  ShippingUpdateView
# ShippingListView
# ShippingDetailView


