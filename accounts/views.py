from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

# from accounts.decorators import required_access
from accounts.forms import RegistrationForm
from accounts.models import User, Profile
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'index.html')


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = "accounts/register.html"
    form_class = RegistrationForm
    model = User
    success_message = "You've registered successfully"
    success_url = reverse_lazy('index')
