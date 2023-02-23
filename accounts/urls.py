from django.urls import path
import accounts
from .views import home, UserCreateView, user_login, customer, designer, inventory, LogoutView



app_name = 'accounts'


urlpatterns = [
    # path('', home, name='home'),
    path('register', UserCreateView.as_view(), name="register"),
    path('', user_login, name='login'),
    path('customer', customer, name='customer'),
    path('designer', designer, name='designer'),
    path('inventory', inventory, name='inventory'),
    path('logout/', LogoutView.as_view(), name="logout"),
]