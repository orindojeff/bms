from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from accounts.decorators import required_access
from accounts.forms import RegistrationForm, LoginForm
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
    success_url = reverse_lazy('accounts:customer')
    

def user_login(request):
    loginform = LoginForm(request.POST or None)
    msg = ''

    if request.method == 'POST':
        if loginform.is_valid():
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.user_type == "FM":
                login(request, user)
                messages.success(request, 'You have been logged in successfully.')
                return redirect('accounts:finance')
            elif user is not None and user.user_type == "IT":
                login(request, user)
                messages.success(request, 'You have been logged in successfully.')
                return redirect('accounts:inventory')
            elif user is not None and user.user_type == "DR":
                login(request, user)
                messages.success(request, 'You have been logged in successfully.')
                return redirect('accounts:driver')
            elif user is not None and user.user_type == "DS":
                login(request, user)
                messages.success(request, 'You have been logged in successfully.')
                return redirect('accounts:designer')
            elif user is not None and user.user_type == "CM":
                login(request, user)
                messages.success(request, 'You have been logged in successfully.')
                return redirect('accounts:customer')
            else:
                msg = 'invalid login credentials'
        else:
            msg = 'error validating form'
    return render(request, 'accounts/login.html', {'form': loginform, 'msg': msg})



class LogoutView(View):

    def get(self, *args, **kwargs):
        logout(self.request)
        messages.success(self.request, "You've logged out successfully.")
        return redirect('accounts:login')


# class ProfileView(SuccessMessageMixin, UpdateView):
#     template_name = 'profile.html'
#     form_class = ProfileModelForm
#     success_url = reverse_lazy('')
#     success_message = "You're profile has been updated successfully"

#     def get_object(self, queryset=None):
#         profile, created = Profile.objects.get_or_create(user=self.request.user)
#         return profile



@required_access(login_url=reverse_lazy('accounts:login'), user_type="IT")
def inventory(request):
    return render(request, 'inventory/index.html')


@required_access(login_url=reverse_lazy('accounts:login'), user_type="FM")
def finance_manager(request):
    return render(request, 'finance.html')


@required_access(login_url=reverse_lazy('accounts:login'), user_type="DR")
def driver(request):
    return render(request, 'driver.html')

@required_access(login_url=reverse_lazy('accounts:login'), user_type="DS")
def designer(request):
    return render(request, 'designer/index.html')

@required_access(login_url=reverse_lazy('accounts:login'), user_type="CM")
def customer(request):
    return render(request, 'customer/index.html')