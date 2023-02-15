from django.urls import path
import accounts
from .views import home, UserCreateView


app_name = 'accounts'


urlpatterns = [
    path('', home, name='home'),
    path('register/', UserCreateView.as_view(), name="register"),
]