from django.urls import path
from . import views


urlpatterns = [
    path('lead-home',views.lead_index, name='lead-home')

]