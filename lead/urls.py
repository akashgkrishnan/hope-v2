from django.urls import path
from . import views


urlpatterns = [
    path('lead-home',views.lead_index, name='lead-home'),
    path('add-management', views.create_management, name='add-management'),
    path('add-leaduser', views.create_leaduser, name='add-leaduser')

]