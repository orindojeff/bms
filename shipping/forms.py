from django import forms
from .models import Location, PickUpStation, UserPickUpStation, Shipping


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name']


class PickUpStationForm(forms.ModelForm):
    class Meta:
        model = PickUpStation
        fields = ['name', 'location']


class UserPickUpStationForm(forms.ModelForm):
    class Meta:
        model = UserPickUpStation
        fields = ['user', 'station']


class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ['order', 'station', 'status', 'driver']
