from django.urls import path
from . import views


urlpatterns = [
    path('teacher-home', views.teacher_home, name='teacher-home')
]