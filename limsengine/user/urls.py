from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from .forms import MyLoginForm




urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html', authentication_form=MyLoginForm), name='login_url'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html',next_page=reverse_lazy('login_url')), name='logout_url')
]