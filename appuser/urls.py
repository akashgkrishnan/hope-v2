from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.app_home, name='home'),
    path('login', auth_views.LoginView.as_view(template_name='appuser/login.html'),name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='appuser/logout.html'), name='logout'),
    path('redirector', views.redirector, name='redirector')
]