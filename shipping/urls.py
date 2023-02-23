from django.urls import path

from . import views

app_name = 'shipping'

urlpatterns = [
    # Location views
    path('locations/', views.LocationListView.as_view(), name='location_list'),
    path('locations/create/', views.LocationCreateView.as_view(), name='location_create'),
    path('locations/<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
    path('locations/<int:pk>/update/', views.LocationUpdateView.as_view(), name='location_update'),
    path('locations/<int:pk>/delete/', views.LocationDeleteView.as_view(), name='location_delete'),

    # PickUpStation views
    path('pickupstations/', views.PickUpStationListView.as_view(), name='pickupstation_list'),
    path('pickupstations/create/', views.PickUpStationCreateView.as_view(), name='pickupstation_create'),
    path('pickupstations/<int:pk>/', views.PickUpStationDetailView.as_view(), name='pickupstation_detail'),
    path('pickupstations/<int:pk>/update/', views.PickUpStationUpdateView.as_view(), name='pickupstation_update'),
    path('pickupstations/<int:pk>/delete/', views.PickUpStationDeleteView.as_view(), name='pickupstation_delete'),

    # UserPickUpStation views
    path('userpickupstations/', views.UserPickUpStationListView.as_view(), name='userpickupstation_list'),
    path('userpickupstations/create/', views.UserPickUpStationCreateView.as_view(), name='userpickupstation_create'),
    path('userpickupstations/<int:pk>/', views.UserPickUpStationDetailView.as_view(), name='userpickupstation_detail'),
    path('userpickupstations/<int:pk>/update/', views.UserPickUpStationUpdateView.as_view(), name='userpickupstation_update'),
    path('userpickupstations/<int:pk>/delete/', views.UserPickUpStationDeleteView.as_view(), name='userpickupstation_delete'),

    # Shipping views
    path('shippings/', views.ShippingListView.as_view(), name='shipping_list'),
    path('shippings/create/', views.ShippingCreateView.as_view(), name='shipping_create'),
    path('shippings/<int:pk>/', views.ShippingDetailView.as_view(), name='shipping_detail'),
    path('shippings/<int:pk>/update/', views.ShippingUpdateView.as_view(), name='shipping_update'),
    # path('shippings/<int:pk>/delete/', views.ShippingDeleteView.as_view(), name='shipping_delete'),
]
