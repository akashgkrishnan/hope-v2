from django.urls import path
from . import views


urlpatterns = [
    path('lead-home',views.lead_index, name='lead-home'),
    path('add-management', views.create_management, name='add-management'),
    path('add-leaduser', views.create_leaduser, name='add-leaduser'),
    path('add-bus', views.create_bus, name='add-bus'),
    path('add-event', views.events , name='add-event'),
    path('add-subject', views.subject_create, name='add-subject'),
    path('add-student', views.add_student, name='add-student'),
    path('add-teacher', views.add_teacher, name='add-teacher'),
    path('departments', views.departments, name='departments')

]